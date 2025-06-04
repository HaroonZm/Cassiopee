from itertools import product
"""
-> は @と表記する
"""

ALL_VARS = {c for c in "abcdefghijk"}

interpret = lambda x: {"T": 1, "F": 0}.get(x)

def eval_expr(expr, env, idx):
    thing = expr[idx]
    meaning = interpret(thing)
    if meaning is not None:
        return meaning, idx+1
    elif thing in ALL_VARS:
        return env[thing], idx+1
    elif thing == "-":
        idx += 1
        val, idx = eval_expr(expr, env, idx)
        return 0 if val else 1, idx
    else:
        idx += 1
        left, idx = eval_expr(expr, env, idx)
        op = expr[idx]
        idx += 1
        right, idx = eval_expr(expr, env, idx)
        idx += 1
        # Custom "operator table" - idiosyncratic!
        op_map = {
            "*": lambda a, b: a & b,
            "+": lambda a, b: a | b,
            "@": lambda a, b: (not a) | b,
        }
        try:
            result = op_map[op](left, right)
        except:
            raise Exception(f"Weird operator:{op}")
        return result, idx

S = input()
VERUM, FALSUM = 1, 0
def brute_mapper(v):
    bits = format(v, "011b")
    return {ch:int(b) for ch, b in zip("abcdefghijk", bits)}
while S != "#":
    S = S.replace("->", "@")
    # Remove double negation non-conventionally
    while "--" in S:
        S = S.replace("--", "")
    try:
        LHS, RHS = S.split("=")
    except ValueError:
        print("Syntax Error")
        S = input()
        continue
    for v in range(1<<11):
        env = brute_mapper(v)
        lval, _ = eval_expr(LHS, env, 0)
        rval, _ = eval_expr(RHS, env, 0)
        if int(bool(lval)) != int(bool(rval)):
            print("NO")
            break
    else:
        print("YES")
    S = input()