import sys

def parse_atomic_table():
    weights = {}
    for line in sys.stdin:
        line=line.strip()
        if line=="END_OF_FIRST_PART":
            break
        symbol, weight = line.split()
        weights[symbol] = int(weight)
    return weights

def parse_formula(formula, weights):
    stack = [0]
    i = 0
    n = len(formula)
    while i < n:
        c = formula[i]
        if c == '(':
            stack.append(0)
            i += 1
        elif c == ')':
            i += 1
            num = 0
            while i < n and formula[i].isdigit():
                num = num*10 + int(formula[i])
                i += 1
            if num == 0:
                num = 1
            val = stack.pop()
            stack[-1] += val * num
        else:
            # parse atom symbol
            if i+1 < n and formula[i+1].islower():
                atom = formula[i:i+2]
                i += 2
            else:
                atom = c
                i += 1
            num = 0
            while i < n and formula[i].isdigit():
                num = num*10 + int(formula[i])
                i += 1
            if num == 0:
                num = 1
            if atom not in weights:
                return None
            stack[-1] += weights[atom]*num
    return stack[0]

def main():
    weights = parse_atomic_table()
    for line in sys.stdin:
        line=line.strip()
        if line=="0":
            break
        val = parse_formula(line, weights)
        if val is None:
            print("UNKNOWN")
        else:
            print(val)

if __name__=="__main__":
    main()