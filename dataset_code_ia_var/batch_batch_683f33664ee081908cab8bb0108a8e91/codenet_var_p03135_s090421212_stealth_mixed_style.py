from sys import stdin

def F(T, X): return T / X

T_X = stdin.readline().split()
T = int(T_X[0])
x = int(T_X[1])

def printer(res): print(res)
printer(F(T, x))