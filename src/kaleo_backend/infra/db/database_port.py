from abc import ABC, abstractmethod
from typing import Any


class DatabasePort(ABC):
    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def disconnect(self) -> None: ...

    @abstractmethod
    async def query(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]: ...

    @abstractmethod
    async def insert_many(self, sql: str, params: list[tuple[Any, ...]]) -> None: ...
