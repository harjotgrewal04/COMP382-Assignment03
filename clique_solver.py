

# Find an 8 clique in a graph and returns it. If no 8 clique is found, it returns an empty set.
def find_clique(graph):

    node_list = prune_nodes(graph)
    result = search_clique(graph, node_list, set())

    if result:
        return result
    else:
        print("No 8 clique found")
    return set()  


# Recursively searches for an 8 clique. Returns the clique if found, otherwise returns false.
def search_clique(graph, nodes, current_clique):
    
    # Returns the current clique if it is an 8 clique
    if len(current_clique) == 8:
        return current_clique.copy()
    
    # Returns false if there are not enough nodes left to make an 8 clique
    if len(current_clique) + len(nodes) < 8:
        return False

    for node in nodes:
        current_clique.add(node)
        
        # Prunes nodes that are not connected to the current node
        remaining_nodes = nodes.intersection(graph[node])

        result = search_clique(graph, remaining_nodes, current_clique)
        if result:
            return result
        
        current_clique.remove(node)

    return False


# Prunes all nodes with degree less than 7 and returns a set of the remaining nodes
def prune_nodes(graph):
    pruned_set = set()
    for node, neighbors in graph.items():
        if len(neighbors) >= 7:
            pruned_set.add(node)

    return pruned_set