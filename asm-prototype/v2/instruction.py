from dataclasses import dataclass
from tagged_pointer import Operand, TaggedPointer

@dataclass(frozen=True)
class Instruction:
    pass


@dataclass(frozen=True)
class Or(Instruction):
    destination: TaggedPointer
    source_1: Operand
    source_2: Operand


@dataclass(frozen=True)
class And(Instruction):
    destination: TaggedPointer
    source_1: Operand
    source_2: Operand


@dataclass(frozen=True)
class Print(Instruction):
    target: Operand
