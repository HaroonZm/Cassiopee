import math

def get_input():
    return int(input())

k = get_input()
n = 512
a = ''

compute = lambda x, y, z: math.factorial(x+y)//math.factorial(y)//math.factorial(x)
i = n-1
while i >= 0:
    v = compute(7, i, 7)
    q, k = divmod(k, v)
    def rep(letter, count):
        return letter * count
    if q != 0:
        a = "FESTIVA" + rep("L", q) + a
    else:
        a = "FESTIVA" + a
    i -= 1

print(f"{a}")