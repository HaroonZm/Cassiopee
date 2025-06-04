from operator import sub
from sys import stdin

def readints(): 
    return map(int, stdin.readline().split())

n, a, b = readints()
print(max(0, sub(b, a) * (n - 2) + 1))