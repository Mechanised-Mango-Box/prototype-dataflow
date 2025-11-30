from dataclasses import dataclass
from typing import List, Set
from collection_type import CollectionType
from scalar_type import ScalarType


@dataclass(frozen=True)
class VariableType:
    scalar: ScalarType
    collection: CollectionType


@dataclass
class TaggedVariable:
    tag: VariableType

    value: object


def similar(*items: TaggedVariable) -> bool:
    if not items:
        return True
    return all(item == items[0] for item in items)


@dataclass
class TaggedPointer:
    label: str


@dataclass
class ImmediateValue:
    value: TaggedVariable


Operand = TaggedPointer
# Operand = TaggedPointer | ImmediateValue
