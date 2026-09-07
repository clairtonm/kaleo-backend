from typing import Any

from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from kaleo_backend.infra.db.database_port import DatabasePort


class PostgresAdapter(DatabasePort):
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url
        self._connection = None

    def connect(self) -> None:
        pool = ConnectionPool(
            conninfo=self.database_url,
            min_size=2,
            max_size=10,
            kwargs={"row_factory": dict_row}
        )

        with pool.connection() as conn:
            self._connection = conn

    def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        with self._connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def insert_many(self, sql: str, params: list[tuple[Any, ...]]) -> None:
        with self._connection.cursor() as cursor:
            cursor.executemany(sql, params)
            self._connection.commit()
