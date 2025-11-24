
from dataclasses import dataclass
from typing import Dict
import uuid
from dataflow import Board
from util_types import Variable


@dataclass
class DataflowMachine:
    board: Board
    node_states: Dict[uuid.UUID, object]
    var_table: Dict[str, Variable]
