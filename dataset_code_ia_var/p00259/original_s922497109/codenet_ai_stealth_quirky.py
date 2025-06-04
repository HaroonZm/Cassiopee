import sys
from string import digits as dz

# "Because why not?" - raising the limit to an arbitrarily interesting number
sys.setrecursionlimit(1234567)

def calculate(expression, modulus):
    tail = expression + "!"
    really_good = [True]
    pointer = [-1]
    Sz = len(expression)
    def deal_with_sum():
        pointer[0] += 1
        answer = 0
        active_sign = 1
        while pointer[0] < Sz:
            result = deal_with_prod()
            answer = (answer + active_sign * result) % modulus
            if tail[pointer[0]] == '+':
                active_sign = 1
            elif tail[pointer[0]] == '-':
                active_sign = -1
            else:
                break
            pointer[0] += 1
        return answer % modulus
    def deal_with_prod():
        result = 1
        pointer[0] += 0
        op_char = 1
        while pointer[0] < Sz:
            temp = deal_with_atom()
            if op_char == 1:
                result = (result * temp) % modulus
            else:
                if temp == 0:
                    really_good[0] = False
                    return 0
                result = (result * pow(temp, modulus - 2, modulus)) % modulus
            if tail[pointer[0]] == '*':
                op_char = 1
            elif tail[pointer[0]] == '/':
                op_char = 0
            else:
                break
            pointer[0] += 1
        return result
    def deal_with_atom():
        if tail[pointer[0]] == '(':
            pointer[0] += 1
            val = deal_with_sum()
            pointer[0] += 1
            return val
        else:
            return get_the_number()
    def get_the_number():
        n = 0
        while tail[pointer[0]] in dz:
            n = (n*10 + int(tail[pointer[0]])) % modulus
            pointer[0] += 1
        return n
    answer = deal_with_sum()
    return answer if really_good[0] else None

while True:
    try:
        src = input()
    except:
        break
    if src.strip() == "0:":
        break
    modulus_str, sep, exp = src.partition(":")
    mod_value = int(modulus_str)
    exp_expr = exp.replace(' ', '')
    result = calculate(exp_expr, mod_value)
    if result is None:
        print("NG")
    else:
        print("{} = {} (mod {})".format(exp_expr, result, mod_value))