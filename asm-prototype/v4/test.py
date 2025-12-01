from typing import Callable, Dict, List
from data import  Word


class Instruction:
    def execute(self, vm: VirtualMachine) -> None:
        raise NotImplementedError()


class Copy(Instruction):
    label_from: str
    label_to: str

    def execute(self, vm: VirtualMachine) -> None:
        var_from = vm.data[self.label_from]
        var_to = vm.data[self.label_to]

        var_to.value = var_from.value

class VirtualMachine:
    """
    MATRTOS Machine
    """

    # Registers
    PC: int
    """Program Counter"""
    # IRA: Word
    # """Interrupt Return Address (Optional)"""

    # Segments
    data: Dict[str, Word]
    instructions: List[Instruction]

    def step(self):
        inst = self.instructions[self.PC]
        inst.execute(self)
