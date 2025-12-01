from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Word:
    """
    16 bit word
    """

    def __add__(self, other: Word) -> Word: raise NotImplementedError()
    def __sub__(self, other: Word) -> Word: raise NotImplementedError()


V2i = Tuple[int, int]


class Container:
    pass


# class Empty(Container):
#     pass


class Scalar(Container):
    value: Word


def walk(rows: int, cols: int):
    for i in range(cols):
        for j in range(rows):
            yield i, j


class Matrix(Container):
    __data: List[List[Word]]

    def size_cols(self) -> int:
        return len(self.__data)

    def size_rows(self) -> int:
        return len(self.__data[0])

    def __getitem__(self, pos: V2i) -> Word:
        return self.__data[pos[0]][pos[1]]

    def __setitem__(self, pos: V2i, item: Word):
        self.__data[pos[0]][pos[1]] = item

    def walk(self):
        return walk(self.size_cols(), self.size_rows())
