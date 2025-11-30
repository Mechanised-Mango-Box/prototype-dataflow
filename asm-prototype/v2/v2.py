from typing import Dict, List
from dataclasses import dataclass
from tagged_pointer import ImmediateValue, TaggedPointer, TaggedVariable, similar
from instruction import And, Instruction, Operand, Or, Print
from collection_type import Matrix, Scalar, Vector
from scalar_type import Bool


@dataclass
class Machine:
    # Segments
    instructions: List[Instruction]
    data: Dict[str, TaggedVariable]  # label -> (tag, value)

    # Special Registers
    pc: int
    # ra: int

    # def get_var(self, operand: Operand) -> TaggedVariable:
    #     match operand:
    #         case ImmediateValue():
    #             return operand.value
    #         case TaggedPointer():
    #             var = self.data.get(operand.label)
    #             assert (var)
    #             return var
    def get_var(self, operand: Operand) -> TaggedVariable:
        var = self.data.get(operand.label)
        assert (var)
        return var


def execute(m: Machine):
    cur_inst = m.instructions[m.pc]

    match cur_inst:
        case Or(d, s1, s2):
            a1, a2, a3 = m.get_var(d), m.get_var(s1), m.get_var(s2)
            assert a1.tag.scalar == Bool
            assert a1.tag.scalar == a2.tag.scalar == a3.tag.scalar

            match a1.tag.collection, a2.tag.collection, a3.tag.collection:
                case Matrix(), Matrix(), Matrix():
                    assert similar(a1, a2, a3)
                    for i in range(a1.tag.collection.rows):
                        for j in range(a1.tag.collection.cols):
                            assert type(a1.value) is List[List[bool]]
                            assert type(a2.value) is List[List[bool]]
                            assert type(a3.value) is List[List[bool]]
                            a1.value[i][j] = a2.value[i][j] and a3.value[i][j]
                case Matrix(), Matrix(), Scalar():
                    assert similar(a1, a2)
                    for i in range(a1.tag.collection.rows):
                        for j in range(a1.tag.collection.cols):
                            assert type(a1.value) is List[List[bool]]
                            assert type(a2.value) is List[List[bool]]
                            a1.value[i][j] = a2.value[i][j] and a3.value

                case Vector():

            match a1, a2, a3:
                case a1, a2, a3 if type(a2.tag.collection) is Matrix:
            if a1.tag.collection == a2.tag.collection:
                if a3.tag.collection == a1.tag.collection or a3.tag.collection == Scalar():
                    pass  # Element-wise

        case And(d, s1, s2):
            pass
        case Print(t):
            print(f"<Print> {t}")
