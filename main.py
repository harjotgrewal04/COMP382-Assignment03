from parser import parse_3sat_formula, is_negated


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
    


if __name__ == "__main__":
    formula_text = input("Enter 3SAT Formula: ")

    clauses = parse_3sat_formula(formula_text, expected_k=8)

    print(clauses)
