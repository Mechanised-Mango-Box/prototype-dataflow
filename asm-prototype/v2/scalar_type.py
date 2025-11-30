from dataclasses import dataclass


@dataclass
class ScalarType:
    pass


@dataclass
class Int(ScalarType):
    pass


@dataclass
class Bool(ScalarType):
    pass


@dataclass
class Decimal(ScalarType):
    pass
