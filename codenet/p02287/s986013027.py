import sys
input = sys.stdin.readline

N = int(input())
btree = list(map(int, input().split()))

for i in range(1, N + 1):
    result = ""
    result += "node {0}: key = {1}, ".format(i, btree[i - 1])
    if i // 2 > 0:
        result += "parent key = {0}, ".format(btree[(i // 2) - 1])
    if i * 2 <= N:
        result += "left key = {0}, ".format(btree[i * 2 - 1])
    if i * 2 + 1 <= N:
        result += "right key = {0}, ".format(btree[i * 2])

    print(result)