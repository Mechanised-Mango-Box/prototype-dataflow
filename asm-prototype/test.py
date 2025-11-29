from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Never

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
    pass


@dataclass(frozen=True)
class Sum(Instruction):
    destination: VariableName
    source_1: Arg
    source_2: Arg


@dataclass(frozen=True)
class Product(Instruction):
    destination: VariableName
    source_1: Arg
    source_2: Arg


class Machine:
    variables: Dict[str, Variable] = {}
    instructions: List[Instruction] = []

    instruction_index: int = 0

    def run(self):
        while True:  # TODO
            instruction: Instruction = self.instructions[self.instruction_index]
            self.execute(instruction)

    def execute(self, instruction: Instruction):
        match instruction:
            case Sum():
                # TODO checks
                self.variables[instruction.destination] = self.get_value(
                    instruction.source_1) * self.get_value(instruction.source_2)
                self.increment_instruction()

            case Product():
                # TODO checks
                self.variables[instruction.destination] = self.get_value(
                    instruction.source_1) * self.get_value(instruction.source_2)
                self.increment_instruction()

            case Instruction(): assert (Never)  # This should never happen

    def get_value(self, variable_name: VariableName) -> Value:
        return self.variables[variable_name]

    def increment_instruction(self):
        self.instruction_index += 1
