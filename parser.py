import re

def change_string( literal: str) -> str:
    lit = literal.strip().replace(" ", "")

    lit = lit.replace("¬", "~")
    if lit.startswith("-"):
        lit = "~" + lit[1:]

    if re.fullmatch(r"x\d+", lit):
        return lit
    
    if re.fullmatch(r"~x\d+", lit):
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