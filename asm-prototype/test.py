from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Tuple, TypeVar

# RegisterName = str
# Value = ImmediateValue | Collection[ImmediateValue]
# ImmediateValue = int| float
# Args = RegisterName | ImmediateValue
Type = Literal["BOOL", "INT", "DECIMAL", "CHAR"]
Opcode = Literal["SUM", "PRODUCT"]

Value = Any

@dataclass(frozen=True)
class Variable:
    tag: Type
    value: Value

VariableName = str
Arg = VariableName | Value


@dataclass(frozen=True)
class Instruction:
    args: Tuple[Arg, ...]


@dataclass(frozen=True)
class Sum(Instruction):
    args: Tuple[VariableName, Arg, Arg]


@dataclass(frozen=True)
class Product(Instruction):
    args: Tuple[VariableName, Arg, Arg]


class Machine:
    variables: Dict[str, Variable]
    instructions: List[Instruction]

    def run(self):
        lineIndex: int = 0
        while True: # TODO
            instruction:Instruction = self.instructions[lineIndex] 
            self.execute(instruction)

    def execute(self, instruction: Instruction):
        match instruction:
            case Sum():
                # TODO checks
                res = instruction.args[1] + instruction.args[2]
                writeToVarName:VariableName = instruction.args[0]
                self.variables[writeToVarName] = 


def foo():
    s: Sum = Sum(("myvar1", "myvar2", 134))
