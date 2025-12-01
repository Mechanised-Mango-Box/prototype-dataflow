from typing import Callable, Dict, List
from data import Container, Matrix, Scalar, Word


class Instruction:
    def execute(self, vm: VirtualMachine) -> None:
        raise NotImplementedError()


class TriArgFn(Instruction):
    label_dest: str
    label_s1: str
    label_s2: str
    fn: Callable[[Word, Word], Word]

    def execute(self, vm: VirtualMachine) -> None:
        dest = vm.data[self.label_dest]
        s1 = vm.data[self.label_s1]
        s2 = vm.data[self.label_s2]

        # S = S + S
        # M = M + S
        # M = M + M

        match dest, s1, s2:
            case Scalar(), Scalar(), Scalar():
                dest.value = s1.value + s2.value

            case Matrix(), Matrix(), Scalar() if dest.size_cols() == s1.size_cols() and dest.size_rows() == s1.size_rows():
                for i, j in dest.walk():
                    dest[i, j] = self.fn(s1[i, j], s2.value)

            case Matrix(), Scalar(), Matrix() if dest.size_cols() == s2.size_cols() and dest.size_rows() == s2.size_rows():
                for i, j in dest.walk():
                    dest[i, j] = self.fn(s1.value, s2[i, j])

            case Matrix(), Matrix(), Matrix() if dest.size_cols() == s1.size_cols() == s2.size_cols() and dest.size_rows() == s1.size_rows() == s2.size_rows():
                for i, j in dest.walk():
                    dest[i, j] = self.fn(s1[i, j], s2[i, j])

            case _:
                raise ValueError("Invalid args")


class VirtualMachine:
    """
    MATRTOS Machine
    """

    # Registers
    PC: int
    """Program Counter"""
    IRA: int
    """Interrupt Return Address (Optional)"""

    # Segments
    data: Dict[str, Container]
    instructions: List[Instruction]

    def step(self):
        inst = self.instructions[self.PC]
        inst.execute(self)
