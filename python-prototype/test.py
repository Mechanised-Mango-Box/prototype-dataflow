import uuid
from dataflow import Board, Edge, Node, NodeType, get_arg_pins, get_result_pins, tick


b = Board({}, {}, {})

n1 = Node(uuid.uuid4(), NodeType.CONSTANT, (0, 0))
b.nodes[n1.id] = n1

n2 = Node(uuid.uuid4(), NodeType.PRINT, (0, 0))
b.nodes[n2.id] = n2

e1 = Edge(get_result_pins(n1)[0], {get_arg_pins(n2)[0]})
b.edges[e1.source] = e1

tick(b)