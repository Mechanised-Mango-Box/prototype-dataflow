from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CollectionType:
    pass


@dataclass(frozen=True)
class Scalar(CollectionType):
    pass


@dataclass(frozen=True)
class Vector(CollectionType):
    length: int


@dataclass(frozen=True)
class Matrix(CollectionType):
    rows: int
    cols: int
