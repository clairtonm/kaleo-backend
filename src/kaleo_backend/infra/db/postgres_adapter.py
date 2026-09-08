from typing import Any

from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool

from kaleo_backend.infra.db.database_port import DatabasePort


class PostgresAdapter(DatabasePort):
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url
        self._pool: AsyncConnectionPool | None = None

    async def connect(self) -> None:
        self._pool = AsyncConnectionPool(
            conninfo=self.database_url,
            min_size=2,
            max_size=10,
            kwargs={"row_factory": dict_row},
            open=False,
        )
        await self._pool.open()

    async def disconnect(self) -> None:
        if self._pool:
            await self._pool.close()
            self._pool = None

    async def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        assert self._pool, "Database not connected"
        async with self._pool.connection() as conn, conn.cursor() as cursor:
            await cursor.execute(sql, params)
            return await cursor.fetchall()

    async def insert_many(self, sql: str, params: list[tuple[Any, ...]]) -> None:
        assert self._pool, "Database not connected"
        async with self._pool.connection() as conn, conn.cursor() as cursor:
            await cursor.executemany(sql, params)
