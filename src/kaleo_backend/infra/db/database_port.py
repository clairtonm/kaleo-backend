from abc import ABC, abstractmethod
from typing import Any


class DatabasePort(ABC):
    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]: ...

    @abstractmethod
    def insert_many(self, sql: str, params: list[tuple[Any, ...]]) -> None: ...
