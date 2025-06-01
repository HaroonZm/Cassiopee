import sys
from string import digits as D

sys.setrecursionlimit(pow(10,6))
def calculate(expression, modulus):
    length = len(expression)
    expression += "$"
    valid = [True]
    position = [0]

    def evaluate():
        result = 0
        operator = '+'
        while position[0] < length:
            val = parse_term()
            if operator == '+':
                result = (result + val) % modulus
            else:
                result = (result - val) % modulus
            if expression[position[0]] not in '+-':
                break
            operator = expression[position[0]]
            position[0] += 1
        return result % modulus

    def parse_term():
        result = 1
        operator = '*'
        while position[0] < length:
            val = parse_factor()
            if operator == '*':
                result = (result * val) % modulus
            else:
                if val == 0:
                    valid[0] = False
                # Fermat's little theorem inverse
                result = (result * pow(val, modulus - 2, modulus)) % modulus
            if expression[position[0]] not in '*/':
                break
            operator = expression[position[0]]
            position[0] += 1
        return result

    def parse_factor():
        if expression[position[0]] == '(':
            position[0] += 1
            val = evaluate()
            position[0] += 1
            return val
        else:
            return parse_number()

    def parse_number():
        val = 0
        while expression[position[0]] in D:
            val = (val * 10 + int(expression[position[0]])) % modulus
            position[0] += 1
        return val

    result = evaluate()
    return result if valid[0] else -1

while True:
    raw = input()
    if raw == "0:":
        break
    mod_str, expr = raw.split(":")
    mod = int(mod_str)
    expr = expr.replace(" ", "")
    ans = calculate(expr, mod)
    if ans == -1:
        print("NG")
    else:
        print(f"{expr} = {ans} (mod {mod})")