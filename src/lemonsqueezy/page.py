from dataclasses import dataclass
from typing import List, TypeVar, Generic, Mapping

T = TypeVar('T')


@dataclass
class Page:
    currentPage: int
    from_: int
    last_page: int
    per_page: int
    to: int
    total: int


@dataclass
class Meta:
    page: Page


@dataclass
class PageResponse(Generic[T]):
    meta: Meta
    data: List[T]
    links: Mapping[str, str]
