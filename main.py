from parser import parse_3sat_formula, is_negated, variable_name
from reduction import convert_to_clique, draw_clique_graph #converts clauses array to a dictionary clique and draws graph
from clique_solver import find_k_clique ##Partner can change variable once they finish

def build_assignment(clique):
    assignment = {}

    for(literal, clause_index) in clique:
        var = parse_3sat_formula(literal)
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

if __name__ == "__main__":
    formula_text = input("Enter 3SAT Formula: ")

    clauses = parse_3sat_formula(formula_text, expected_k=8)

    print("Parsed clauses:" , clauses)

    # hardcoding test for part 5 until part 3 and 4 are done
    test_clauses = [
        ["x1", "x2", "x3"],
        ["~x1", "x2", "x4"],
        ["x1", "~x2", "x5"],
        ["x2", "x3", "~x4"],
        ["~x3", "x4", "x6"],
        ["x1", "~x5", "x6"],
        ["~x2", "x5", "x6"],
        ["x3", "~x4", "~x6"]
    ]

    test_assignment = {
        "x1": True, "x2": True, "x3": True,
        "x4": False, "x5": True, "x6": True,
    }
    



