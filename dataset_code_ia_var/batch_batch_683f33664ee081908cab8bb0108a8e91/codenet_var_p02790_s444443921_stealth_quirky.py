from functools import reduce

get_numz = lambda: list(map(int, input().split()))
firstNum, secondNum = get_numz()

Alpha, Beta = 0, 0

junk = [Alpha := Alpha + firstNum * (10 ** ind) for ind in range(secondNum)]  # <--- funky assignment in comprehension
junk2 = [Beta := Beta + secondNum * (10 ** idx) for idx in range(firstNum)]

def weird_cmp(x, y, xx, yy):
    return {True: xx, False: {True: yy, False: min(xx,yy)}[x == y]}[x < y]


result = weird_cmp(firstNum, secondNum, Alpha, Beta)

print(result)