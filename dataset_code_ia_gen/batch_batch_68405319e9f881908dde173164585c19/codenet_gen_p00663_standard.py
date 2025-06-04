import sys

def parse_expression(s):
    # Parses the expression string into list of clauses, each clause is list of literals
    # Example: "(B&B&f)|(~d&~i&i)|(~v&i&~V)"
    clauses = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '(':
            j = i+1
            cnt = 1
            while j < n and cnt > 0:
                if s[j] == '(':
                    cnt += 1
                elif s[j] == ')':
                    cnt -= 1
                j += 1
            clause_str = s[i+1:j-1]  # inside parentheses
            literals = clause_str.split('&')
            clauses.append(literals)
            i = j
            if i < n and s[i] == '|':
                i += 1
        else:
            i += 1
    return clauses

def solve_sat_en_3(clauses):
    # Each clause has exactly 3 literals combined with '&' (AND).
    # The whole expression is clauses combined with '|' (OR).
    # expression = OR of AND of 3 literals.
    # We want to see if there exists an assignment to variables to make expression True,
    # i.e. at least one clause is True.
    # A clause is True iff all 3 literals are True.
    # So find if there exists an assignment making at least one clause True.
    
    # We'll try each clause independently:
    # for each clause (AND of 3 literals), can we find an assignment that makes all literals True?
    # If yes, then overall expression is True.
    
    # For a clause l1 & l2 & l3,
    # each literal is either var or ~var.
    # To satisfy literal:
    #   var means variable True
    #   ~var means variable False
    # Check for conflicts inside clause:
    # For clause to be satisfiable: no variable conflicts inside the clause
    
    for clause in clauses:
        assignment = {}
        satisfiable = True
        for lit in clause:
            if lit.startswith('~'):
                var = lit[1]
                val = False
            else:
                var = lit[0]
                val = True
            if var in assignment:
                if assignment[var] != val:
                    satisfiable = False
                    break
            else:
                assignment[var] = val
        if satisfiable:
            return True
    return False

def main():
    input = sys.stdin.read().splitlines()
    for line in input:
        if line == '#':
            break
        clauses = parse_expression(line)
        print("yes" if solve_sat_en_3(clauses) else "no")

if __name__ == "__main__":
    main()