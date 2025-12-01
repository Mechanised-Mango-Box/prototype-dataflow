from dataclasses import dataclass
from typing import Callable, Generic, List, Tuple, TypeVar


@dataclass
class Word:
    pass


# @dataclass
# class Bool(Word):
#     pass


@dataclass
class Char(Word):
    pass


@dataclass
class Int(Word):
    pass


@dataclass
class Decimal(Word):
    pass

V = TypeVar("V", bound=Word)

Pos = Tuple[int, int]


class Scalar(Word, Generic[V]):
    value: V


class Matrix(Word, Generic[V]):
    __data: List[List[V]]

    def size_cols(self) -> int:
        return len(self.__data)

    def size_rows(self) -> int:
        return len(self.__data[0])

    def __getitem__(self, pos: Pos) -> V:
        return self.__data[pos[0]][pos[1]]

    def __setitem__(self, pos: Pos, item: V):
        self.__data[pos[0]][pos[1]] = item
