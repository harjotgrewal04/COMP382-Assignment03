import re

def change_string( literal: str) -> str:
    lit = literal.strip().replace(" ", "")

    lit = lit.replace("¬", "~")
    if lit.startswith("-"):
        lit = "~" + lit[1:]

    if re.fullmatch(r"[xX]\d+", lit):
        return lit
    
    if re.fullmatch(r"~[xX]\d+", lit):
        return lit
    
    raise ValueError(f"Invalid literal format: {literal}")

def is_negated(literal: str) -> bool:
    literal = change_string(literal)
    return literal.startswith("~")

def variable_name(literal: str) -> str:
    literal = change_string(literal)
    return literal[1:] if literal.startswith("~") else literal

def parse_clause(clause_text: str) -> list[str]:
    
    text = clause_text.strip()
    
    if text.startswith("(") and text.endswith(")"):
        text = text[1:-1].strip()

    parts = re.split(r"\s*(?:v|V|OR|or)\s*", text)

    if len(parts) != 3:
        raise ValueError(f"Each clause must contain exactly three literals. Currently: {clause_text}")
    
    literals = [change_string(part) for part in parts]
    return literals

def parse_formula(formula_text: str) -> list[list[str]]:
    text = formula_text.strip()

    if not text:
        raise ValueError("Formula is empty")
    
    clause_matches = re.findall(r"\([^()]+\)", text)

    if clause_matches:
        clauses=[parse_clause(clause) for clause in clause_matches]
        return clauses
    
    raw_clauses = re.split(r"\s*(?:\^|AND|and)\s*", text)
    
    clauses=[parse_clause(clause) for clause in raw_clauses if clause.strip()]
    return clauses

def validate_3sat_instance(clauses: list[list[str]], expected_k: int | None = None) -> None:

    if not clauses:
        raise ValueError("Clauses not found")
    
    for i, clause in enumerate(clauses, start=1):
        if len(clause) != 3:
            raise ValueError(f"Clause C{i} does not have exactly three literals: {clause}")
        
    if expected_k is not None and len(clauses) != expected_k:
        raise ValueError(f"Expected exactly {expected_k} clauses, but found {len(clauses)}.")
    
def parse_3sat_formula(formula_text: str, expected_k: int | None = None) -> list[list[str]]:
   
    clauses = parse_formula(formula_text)

    validate_3sat_instance(clauses, expected_k=expected_k)
    return clauses

if __name__ == "__main__":
    example = """
    (x1 v x2 v x3) ^
    (~x1 v x2 v x4) ^
    (x1 v ~x2 v x5) ^
    (x2 v x3 v ~x4) ^
    (~x3 v x4 v x6) ^
    (x1 v ~x5 v x6) ^
    (~x2 v x5 v x6) ^
    (x3 v ~x4 v ~x6)
    """

    clauses = parse_3sat_formula(example, expected_k=8)

    print("Parsed clauses:")
    for i, clause in enumerate(clauses, start=1):
        print(f"C{i}: {clause}")

    print("\nLiteral helper examples:")
    print("normalize_literal('¬x4') ->", change_string("¬x4"))
    print("is_negated('~x4') ->", is_negated("~x4"))
    print("variable_name('~x4') ->", variable_name("~x4"))

