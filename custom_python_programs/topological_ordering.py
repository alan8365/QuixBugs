
def topological_ordering(nodes):
    ordered_nodes = [node for node in nodes if not node.incoming_nodes]

    while ordered_nodes:
        node = ordered_nodes.pop(0)
        for nextnode in node.outgoing_nodes:
            nextnode.incoming_nodes.remove(node)
            if not nextnode.incoming_nodes and nextnode not in ordered_nodes:
                ordered_nodes.append(nextnode)

    return ordered_nodes


