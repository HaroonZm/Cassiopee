import sys
sys.setrecursionlimit(1010)

N = int(input())
src = []
for i in range(N):
    k = int(input())
    s = input()
    src.append((s, []))
    if i == 0:
        continue
    src[k-1][1].append(i)

stack = [(0, 0)]
while stack:
    i, depth = stack.pop()
    s, ch = src[i]
    print('.' * depth + s)
    for c in reversed(ch):
        stack.append((c, depth+1))