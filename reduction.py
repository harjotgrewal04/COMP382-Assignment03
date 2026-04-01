import parser as ps
# the clauses array should look like: clauses = [["x1","~x2","x3"],["~x1","x6","x4"],...]

# Creates an array that holds each literal and its respective clause number
def create_vertices(clauses):
    vertices = []
    clause_index = 0

    for clause in clauses:
        literal_index = 0

        for literal in clause:                              
            vertices.append((literal,clause_index))
            literal_index += 1

        clause_index += 1

    return vertices

# checks if a literal is a compliment of the other (ex. X1 and ~X1) if it is, thne there is a conflict
def is_literal_conflict(literal1,literal2):

    v1 = ps.variable_name(literal1)
    v2 = ps.variable_name(literal2)
    n1 = ps.is_negated(literal1)
    n2 = ps.is_negated(literal2)

    if (v1 == v2) and (n1 != n2):
        return True
    else:
        return False

# creates a dictionary that holds the tuple as a key (ex. ("X1",0)) and the pair is every vertice that is connected to this vertice
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

            graph[vert1].add(x2)
            graph[vert2].add(x1)

    return graph


# checking = is_literal_conflict("~X2","~X2")
# if checking:
#     print("there is conflict between ~X2 and ~X2")
# else:
#     print("no conflict")


#arr = [["X1","~X2","X3"],["~X1","X3","X5"],["~X2","X6","X8"],["X1","X9","X16"]]

def convert_to_clique(cl_array):
    vert_arr = create_vertices(cl_array)
    clique = create_graph(vert_arr)

    return clique

#print(create_graph(vert_arr))

