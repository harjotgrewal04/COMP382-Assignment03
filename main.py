from parser import parse_3sat_formula



def build_assignment(clique):
    assignment = {}

    for(_, (var, isNeg)) in clique:
        value = not isNeg

        if var in assignment and assignment[var] != value:
            raise ValueError(f"Contradiction for {var}")
        
        assignment[var] = value

        return assignment
    







formula = """
(x1 v x2 v x3) ^
(~x1 v x2 v x4) ^
(x1 v ~x2 v x5) ^
(x2 v x3 v ~x4) ^
(~x3 v x4 v x6) ^
(x1 v ~x5 v x6) ^
(~x2 v x5 v x6) ^
(x3 v ~x4 v ~x6)
"""

clauses = parse_3sat_formula(formula, expected_k=8)
print(clauses)