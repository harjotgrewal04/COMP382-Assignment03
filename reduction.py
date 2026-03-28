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


def is_literal_conflict(literal1,literal2):

    var1 = ps.variable_name(literal1)
    var2 = ps.variable_name(literal2)

    if var1 != var2:
        return False
    
    else:
        return True



