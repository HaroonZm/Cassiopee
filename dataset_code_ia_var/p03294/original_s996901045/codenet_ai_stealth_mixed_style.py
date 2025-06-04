import math
from functools import reduce as red

def g(a, b):
    while b: a, b = b, a % b
    return a

LAMBDA_LCM = lambda x, y: x*y // g(x, y)

def main():
    N = eval(input())
    arr = list(map(int, input().split()))
    # Calcul du PPCM avec une approche différente
    l = red(LAMBDA_LCM, arr)
    res = 0
    [res := res + ((l-1)%x) for x in arr]
    print(res)

if __name__ == '__main__':
    main()