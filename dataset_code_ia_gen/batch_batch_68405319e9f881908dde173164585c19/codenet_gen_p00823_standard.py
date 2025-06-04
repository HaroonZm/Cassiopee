import sys
import re

def main():
    weights = {}
    for line in sys.stdin:
        line=line.strip()
        if line=="END_OF_FIRST_PART":
            break
        if not line:
            continue
        symbol, w = line.split()
        weights[symbol] = int(w)

    pattern_atom = r'[A-Z][a-z]?'
    pattern_num = r'\d{1,2}'
    formula_lines = []
    for line in sys.stdin:
        line=line.strip()
        if line=="0":
            break
        formula_lines.append(line)

    for formula in formula_lines:
        try:
            total = parse_formula(formula, weights)
            print(total)
        except:
            print("UNKNOWN")

def parse_formula(formula, weights):
    pos = 0
    n = len(formula)

    def parse_atom():
        nonlocal pos
        if pos>=n:
            raise ValueError
        if not formula[pos].isupper():
            raise ValueError
        sym=formula[pos]
        pos+=1
        if pos<n and formula[pos].islower():
            sym+=formula[pos]
            pos+=1
        return sym

    def parse_num():
        nonlocal pos
        start=pos
        while pos<n and formula[pos].isdigit():
            pos+=1
        if start==pos:
            return 1
        num=int(formula[start:pos])
        if num<2 or num>99:
            raise ValueError
        return num

    def helper():
        nonlocal pos
        subweights = {}
        while pos<n:
            c = formula[pos]
            if c=='(':
                pos+=1
                inner = helper()
                if pos>=n or formula[pos]!=')':
                    raise ValueError
                pos+=1
                m = parse_num()
                for k,v in inner.items():
                    subweights[k] = subweights.get(k,0)+v*m
            elif c==')':
                break
            elif c.isupper():
                sym = parse_atom()
                if sym not in weights:
                    raise ValueError
                m = parse_num()
                subweights[sym] = subweights.get(sym,0)+m
            else:
                raise ValueError
        return subweights

    counts = helper()
    if pos!=n:
        raise ValueError
    total_weight = 0
    for k,v in counts.items():
        total_weight+=weights[k]*v
    return total_weight

if __name__ == "__main__":
    main()