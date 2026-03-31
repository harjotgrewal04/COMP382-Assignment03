def build_assignment(clique):
    assignment = {}

    for(_, (var, isNeg)) in clique:
        value = not isNeg

        if var in assignment and assignment[var] != value:
            raise ValueError(f"Contradiction for {var}")
        
        assignment[var] = value

        return assignment