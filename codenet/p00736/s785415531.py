def parseParenthesis(formula):
    pos = 0
    count = 0
    while True:
        if formula[pos] == '(':
            count += 1
        elif formula[pos] == ')':
            count -= 1
        elif count == 1 and (formula[pos] == '+' or formula[pos] == '*'):
            sign = formula[pos]
            formulaA = formula[1:pos]
            formulaB = formula[pos + 1: -1]
            return formulaA, sign, formulaB
        pos += 1

def eval_or(a, b):
    if a == '0':
        return b
    elif a == '1':
        return '1' if b == '0' else b
    elif a == '2':
        return '2'

def eval_and(a, b):
    if a == '0':
        return '0'
    elif a == '1':
        return '0' if b == '0' else '1'
    elif a == '2':
        return b

def eval_neg(a):
    if a == '1':
        return '1'
    return '2' if a == '0' else '0'

def evaluate(formula, p, q, r):
    if formula == '0' or formula == '1' or formula == '2':
        return formula
    if formula == 'P':
        return p
    if formula == 'Q':
        return q
    if formula == 'R':
        return r

    if formula[0] == '(':
        formulaA, sign, formulaB = parseParenthesis(formula)
        evalA = evaluate(formulaA, p, q, r)
        evalB = evaluate(formulaB, p, q, r)
        if sign == '+':
            return eval_or(evalA, evalB)
        elif sign == '*':
            return eval_and(evalA, evalB)
    elif formula[0] == '-':
        return eval_neg(evaluate(formula[1:], p, q, r))

if __name__ == '__main__':
    while True:
        formula = input().strip()
        if formula == '.':
            break

        count = 0
        for p in range(3):
            for q in range(3):
                for r in range(3):
                    if evaluate(formula, str(p), str(q), str(r)) == '2':
                        count += 1
        print(count)