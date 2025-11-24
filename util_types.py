from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple


Vector2 = Tuple[float, float]


class Nothing:
    pass

class VariableType(Enum):
    NONE = auto,
    BOOL = auto(),
    STRING = auto()


@dataclass
class Variable:
    tag = VariableType
    value = object