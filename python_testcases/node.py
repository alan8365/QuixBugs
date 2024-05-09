class Node:
    def __init__(
        self,
        value=None,
        successor=None,
        successors=[],
        predecessors=[],
        incoming_nodes=[],
        outgoing_nodes=[],
    ):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def __repr__(self) -> str:
        return f"Node: {self.value}"
