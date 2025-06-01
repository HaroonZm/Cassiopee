import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = [int(x) - 1 for x in input().split()]
exist = [0] * 2021
for x in X:
    exist[x] += 1
for a in A:
    where = X[a]
    if where != 2019 and exist[where + 1] == 0:
        exist[where] -= 1
        exist[where + 1] += 1
        X[a] += 1
for x in X:
    print(x)