import parser as ps
import networkx as nx
import matplotlib.pyplot as plt

# Creates an array that holds each literal and its respective clause number
def create_vertices(clauses):
    vertices = []
    clause_index = 0

    for clause in clauses:

        for literal in clause:                              
            vertices.append((literal,clause_index))    

        clause_index += 1

    return vertices

# checks if a literal is a compliment of the other (ex. X1 and ~X1) if it is, then there is a conflict
def is_literal_conflict(literal1,literal2):

    v1 = ps.variable_name(literal1)
    v2 = ps.variable_name(literal2)
    n1 = ps.is_negated(literal1)
    n2 = ps.is_negated(literal2)

    if (v1 == v2) and (n1 != n2):
        return True
    else:
        return False

# creates a dictionary that holds tuples from vertices array as keys (ex. ("X1",0)) and values are every other tuple that can form an edge with a key
def create_graph(vertices):
    graph = {}
    
    for tuple in vertices:
        graph.setdefault(tuple, set())

    for x in range(len(vertices)):
        vert1 = vertices[x]
        x1, cl_num1 = vertices[x]

        for y in range(x+1, len(vertices)):
            vert2 = vertices[y]
            x2, cl_num2 = vertices[y]
            
            if cl_num1 == cl_num2:
                continue
            if is_literal_conflict(x1,x2):
                continue

            graph[vert1].add(vert2)
            graph[vert2].add(vert1)

    return graph


# can be called and it converts the input to clique
def convert_to_clique(cl_array):
    vert_arr = create_vertices(cl_array)
    clique = create_graph(vert_arr)

    return clique


# draws the graph (needs both networkx and matplotlib dependencies to work). Also need to first convert clauses to clique, then pass the clique to this function.
def draw_clique_graph(clique):

    G = nx.Graph()
    for key, values in clique.items():
        for v in values:
            G.add_edge(key, v)

    layout = nx.spring_layout(G)

    nx.draw(G, layout, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray")
    plt.show()
