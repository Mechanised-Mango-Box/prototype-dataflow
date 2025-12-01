from typing import Dict, List
from var import Matrix, Scalar, Word


class Instruction:
    def execute(self, vm: VirtualMachine) -> None:
        raise NotImplementedError()


class Add(Instruction):
    label_dest: str
    label_s1: str
    label_s2: str

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
                for i in range(dest.size_cols()):
                    for j in range(dest.size_rows()):
                        dest[i, j] = s1[i, j] + s2
            case Matrix(), Matrix(), Matrix() if dest.size_cols() == s1.size_cols() == s2.size_cols() and dest.size_rows() == s1.size_rows() == s2.size_rows():
                for i in range(dest.size_cols()):
                    for j in range(dest.size_rows()):
                        dest[i, j] = s1[i, j] + s2[i, j]


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
    data: Dict[str, Word]
    instructions: List[Instruction]

    def step(self):
        inst = self.instructions[self.PC]
        inst.execute(self)
