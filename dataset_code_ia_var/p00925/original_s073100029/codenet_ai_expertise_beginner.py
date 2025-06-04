s = input()
l = len(s)

def parse1(s):
    cur = 0
    num = 0
    res = 0
    op = '+'
    while cur < len(s):
        if s[cur] == '+' or s[cur] == '*':
            if op == '+':
                res = res + num
            else:
                res = res * num
            num = 0
            op = s[cur]
        else:
            num = num * 10 + int(s[cur])
        cur = cur + 1
    if op == '+':
        res = res + num
    else:
        res = res * num
    return res

def parse2(s):
    cur = 0

    def number():
        nonlocal cur
        n = int(s[cur])
        cur = cur + 1
        return n

    def term():
        nonlocal cur
        result = number()
        while cur < l and s[cur] == '*':
            cur = cur + 1
            result = result * number()
        return result

    def expr():
        nonlocal cur
        result = term()
        while cur < l and s[cur] == '+':
            cur = cur + 1
            result = result + term()
        return result

    return expr()

v = int(input())
r1 = (parse1(s) == v)
r2 = (parse2(s) == v)
if r1 and r2:
    print("U")
elif r2:
    print("M")
elif r1:
    print("L")
else:
    print("I")