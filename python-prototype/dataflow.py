from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Dict, List, Literal, Never, Optional, Set, Tuple, cast
import uuid
from util_types import VariableType, Vector2

# region Pin


@dataclass(eq=True, frozen=True)
class PinID:
    owner: uuid.UUID
    label: str
    type: VariableType

# region Edge


@dataclass
class Edge:
    """
    One to Many
    """
    source: PinID
    sinks: Set[PinID]

# region Node


@dataclass
class Node:
    id: uuid.UUID
    tag: NodeType

    position: Vector2


class NodeType(Enum):
    PRINT = auto()
    CONSTANT = auto()
    LOGICAL_AND = auto()
    LOGICAL_OR = auto()


def get_arg_pins(node: Node) -> Tuple[PinID, ...]:
    match node.tag:
        case NodeType.PRINT:
            return (PinID(node.id, "input", VariableType.STRING),)
        case NodeType.CONSTANT:
            return ()
        case NodeType.LOGICAL_AND:
            return (PinID(node.id, "in_a", VariableType.BOOL), PinID(node.id, "in_b", VariableType.BOOL))
        case NodeType.LOGICAL_OR:
            return (PinID(node.id, "in_a", VariableType.BOOL), PinID(node.id, "in_b", VariableType.BOOL))
    raise NotImplementedError()


def get_result_pins(
        node: Node) -> Tuple[PinID, ...]:
    match node.tag:
        case NodeType.PRINT:
            return ()
        case NodeType.CONSTANT:
            return (PinID(node.id, "data", VariableType.BOOL),)
        case NodeType.LOGICAL_AND:
            return (PinID(node.id, "out", VariableType.BOOL),)
        case NodeType.LOGICAL_OR:
            return (PinID(node.id, "out", VariableType.BOOL),)
    raise NotImplementedError()


def get_result(node: Node) -> Optional[Any]:
    match node.tag:
        case NodeType.PRINT:
            return Never
        case NodeType.CONSTANT:
            return "PLACEHOLDER!!"
    raise NotImplementedError()


def has_output(node: Node) -> bool:
    return get_result(node) is not None


def generate_results(node: Node) -> None:
    print(f"GENERATE RESULTS FOR: {node}")  # TODO PLACEHOLDER
    # Pattern match on type -> return node's result


class Actuator(ABC):
    @abstractmethod
    def actuate(self) -> None: raise NotImplementedError()

# region Board


@dataclass
class Board:
    nodes: Dict[uuid.UUID, Node]  # <NodeID, Node>
    edges: Dict[PinID, Edge]  # <Pin, Edge>
    # TODO Any should be a limtied set of custom(?) types
    user_variables: Dict[str, Any]
    # special_variables: # this should be things like player position


def propagate(board: Board) -> None:
    frontier: List[Node] = []

    # Add all nodes with no dependencies to frontier
    for node in board.nodes.values():
        if len(get_arg_pins(node)) == 0:
            frontier.append(node)

    # BFS-like over nodes
    while len(frontier) != 0:
        found_any_processable_node: bool = False
        for node in frontier:
            if dependencies_fulfilled(board, node):
                generate_results(node)
                frontier.remove(node)
                found_any_processable_node = True
                break

        if not found_any_processable_node:
            raise Exception("Invalid DAG (probs? deadlock/cycle)")


def dependencies_fulfilled(board: Board, node: Node) -> bool:
    """
    All args have been connected and have results
    """
    input_pins = get_arg_pins(node)

    if len(get_arg_pins(node)) == 0:
        return True  # Has no dependencies

    for arg_pin in input_pins:
        # Go back up the chain:
        # [source node] -----> (edge) -----> [node]
        source_edge: Edge | None = board.edges.get(arg_pin)
        if source_edge is None:
            return False
        source_node: Node = board.nodes[source_edge.source.owner]

        if not has_output(source_node):
            return False

    return True


def tick(board: Board) -> None:
    """
    TODO cleanup
    1. snapshot world / load sensor data
    2. propagate
    3. tick actuators
    """
    # TODO snapshot data

    propagate(board)

    for node in board.nodes:
        if issubclass(type(node), Actuator):
            actuator: Actuator = cast(Actuator, node)
            actuator.actuate()
