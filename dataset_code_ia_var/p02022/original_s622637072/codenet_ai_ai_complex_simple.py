from functools import reduce
from operator import mul
N,M=map(int,(__import__('sys').stdin.readline()).split())
A=list(map(int,(__import__('sys').stdin.readline()).split()))
B=list(map(int,(__import__('sys').stdin.readline()).split()))
f=lambda x:reduce(lambda a,b:a+b,x)
print(reduce(mul,[f(A),f(B)]))