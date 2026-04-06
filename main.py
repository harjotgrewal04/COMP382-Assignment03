from parser import parse_3sat_formula, is_negated, variable_name
from reduction import convert_to_clique, draw_clique_graph #converts clauses array to a dictionary clique and draws graph
from clique_solver import find_clique

def build_assignment(clique):
    assignment = {}

    for (literal, clause_index) in clique:
        var = variable_name(literal)   
        isNeg = is_negated(literal)

        value = not isNeg

        if var in assignment and assignment[var] != value:
            raise ValueError(f"Contradiction for {var}")
        
        assignment[var] = value

    return assignment  

def verify_solution(clauses, assignment):
    # assume whole formula is satisfied
    allLiteralsSatisfied = True

    # loop through each clause numbering them from 1
    for i, clause in enumerate(clauses, start=1):

        satisfied_literals = [];

        # check each literal inside the current clause
        for literal in clause:

            # get variable name from literal and check if its negative
            var = variable_name(literal)
            neg = is_negated(literal)

            # evaluate literal using assignment
            if neg:
                value = not assignment[var]
            else:
                value = assignment[var]

            if value:
                satisfied_literals.append(literal)

        # if one literal is true then the whole clause is true because of 'OR'
        if satisfied_literals:
            print("C", i, ":", clause, " -> true")
        # if no literals were true then the whole clause is false
        else:
            print("C", i, ":", clause, " -> false")
            allLiteralsSatisfied = False

    #print result
    if allLiteralsSatisfied:
        print("All clauses satisfied, valid solution")
    else:
        print("Not all clauses are satisfied")

    return allLiteralsSatisfied

def complete_assignment(clauses, assignment):
    # make copy so original is not changed
    completed = assignment.copy();

    # loop through each clause then through each literal
    for clause in clauses:
        for literal in clause:
            var = variable_name(literal)
            # if variable not already in assignment give default value False
            if var not in completed:
                completed[var] = False

    return completed



if __name__ == "__main__":
    formula_text = input("Enter 3SAT Formula: ")

    clauses = parse_3sat_formula(formula_text, expected_k=8)

    print("Parsed clauses:" , clauses)


    # Converting to a clique graph
    clique_graph = convert_to_clique(clauses)
    
    # Finding an 8-clique
    clique = find_clique(clique_graph)

    # Process of building an assignment by converting selection of nodes back to a solution of the original input 3SAT instance
    if clique:
        print("\nClique found: ")
        for node in clique:
            print(node)

        assignment = build_assignment(clique)

        print("\nAssignment:")
        for var, val in assignment.items():
            print(f"{var} = {val}")
    else:
        print("no solution")

    draw_clique_graph(clique_graph)




