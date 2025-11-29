from dataclasses import dataclass
from typing import Dict, List, Literal, Callable, Tuple

InstructionOutcome = Literal["SUCCESS", "ERROR", "NEVER"]

Type = Literal["BOOL", "INT", "DECIMAL"]
Opcode = Literal["SUM", "PRODUCT", "PRINT"]

Value = bool | int | float


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


@dataclass(frozen=True)
class Print(Instruction):
    source: VariableName


# Dispatch table: (Opcode, Type) -> function
OPERATIONS: Dict[Tuple[Opcode, Type], Callable[[Value, Value], Value]] = {
    ("SUM", "INT"): lambda a, b: a + b,
    ("SUM", "DECIMAL"): lambda a, b: a + b,
    ("SUM", "BOOL"): lambda a, b: a or b,
    ("PRODUCT", "INT"): lambda a, b: a * b,
    ("PRODUCT", "DECIMAL"): lambda a, b: a * b,
    ("PRODUCT", "BOOL"): lambda a, b: a and b,
}

PROMOTION: Dict[Tuple[Type, Type], Type] = {
    ("INT", "DECIMAL"): "DECIMAL",
    ("DECIMAL", "INT"): "DECIMAL",
    ("INT", "INT"): "INT",
    ("DECIMAL", "DECIMAL"): "DECIMAL",
    ("BOOL", "BOOL"): "BOOL",
    ("INT", "BOOL"): "INT",
    ("BOOL", "INT"): "INT",
    ("DECIMAL", "BOOL"): "DECIMAL",
    ("BOOL", "DECIMAL"): "DECIMAL",
}


class Machine:
    def __init__(self):
        self.variables: Dict[VariableName, Variable] = {}
        self.instructions: List[Instruction] = []
        self.instruction_index: int = 0

    def run(self):
        while self.instruction_index < len(self.instructions):
            instruction: Instruction = self.instructions[self.instruction_index]
            outcome = self.execute(instruction)
            if outcome == "ERROR":
                print(
                    f"Error executing instruction at index {self.instruction_index}")
                break

    def get_tag(self, value: Value) -> Type:
        if type(value) is int:
            return "INT"
        if type(value) is float:
            return "DECIMAL"
        if type(value) is bool:
            return "BOOL"
        raise TypeError("Unknown type")

    def execute(self, instruction: Instruction) -> InstructionOutcome:
        match instruction:
            case Sum(destination, source_1, source_2):
                value_1 = self.get_arg_value(source_1)
                value_2 = self.get_arg_value(source_2)
                tag1 = self.get_tag(value_1)
                tag2 = self.get_tag(value_2)
                result_tag = PROMOTION.get((tag1, tag2))
                if not result_tag:
                    return "ERROR"
                func = OPERATIONS.get(("SUM", result_tag))
                if not func:
                    return "ERROR"
                self.variables[destination] = Variable(
                    result_tag, func(value_1, value_2))
                self.increment_instruction()
                return "SUCCESS"

            case Product(destination, source_1, source_2):
                value_1 = self.get_arg_value(source_1)
                value_2 = self.get_arg_value(source_2)
                tag1 = self.get_tag(value_1)
                tag2 = self.get_tag(value_2)
                result_tag = PROMOTION.get((tag1, tag2))
                if not result_tag:
                    return "ERROR"
                func = OPERATIONS.get(("PRODUCT", result_tag))
                if not func:
                    return "ERROR"
                self.variables[destination] = Variable(
                    result_tag, func(value_1, value_2))
                self.increment_instruction()
                return "SUCCESS"

            case Print(source):
                value = self.get_value(source)
                tag = self.variables[source].tag
                print(f"[PRINT] {source}: {tag} = {value}")
                self.increment_instruction()
                return "SUCCESS"

            case Instruction():
                return "NEVER"

    def get_arg_value(self, arg: Arg) -> Value:
        if isinstance(arg, str):
            return self.get_value(arg)
        return arg

    def get_value(self, variable_name: VariableName) -> Value:
        return self.variables[variable_name].value

    def increment_instruction(self):
        self.instruction_index += 1


if __name__ == "__main__":
    m = Machine()

    # Initialize variables
    m.variables["counter"] = Variable("INT", 0)
    m.variables["total"] = Variable("DECIMAL", 123.456)
    m.variables["flag"] = Variable("BOOL", False)

    # Add instructions
    m.instructions = [
        Sum(destination="counter", source_1=10,
            source_2=20),        # counter = 30
        Product(destination="total", source_1="total",
                source_2=2.5),  # total = 308.64
        Sum(destination="flag", source_1=True,
            source_2=False),      # flag = True
        Sum(destination="counter", source_1="counter",
            source_2=10),  # counter = 40
        # print counter
        Print(source="counter"),
        # print total
        Print(source="total"),
        # print flag
        Print(source="flag"),


        Sum(destination="counter", source_1="counter", source_2="total")
    ]

    m.run()

    print("Final state of variables:")
    for name, var in m.variables.items():
        print(f"{name}: {var.tag} = {var.value}")
