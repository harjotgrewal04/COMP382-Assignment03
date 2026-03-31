from parser import parse_3sat_formula



def build_assignment(clique):
    assignment = {}

    for(_, (var, isNeg)) in clique:
        value = not isNeg

        if var in assignment and assignment[var] != value:
            raise ValueError(f"Contradiction for {var}")
        
        assignment[var] = value

        return assignment
    





if __name__ == "__main__":
    formula_text = input("Enter 3SAT Formula: ")

    clauses = parse_3sat_formula(formula_text, expected_k=8)

    print(clauses)
