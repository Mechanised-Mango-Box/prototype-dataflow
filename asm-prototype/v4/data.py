from dataclasses import dataclass
from typing import Tuple

WordValue = Tuple[bool, bool, bool, bool, bool, bool, bool, bool,
            bool, bool, bool, bool, bool, bool, bool, bool]


@dataclass
class Word:
    value: WordValue

    def __add__(self, other: Word) -> Word: raise NotImplementedError()
    def __sub__(self, other: Word) -> Word: raise NotImplementedError()
