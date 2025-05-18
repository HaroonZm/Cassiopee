n = int(input())
v = []
[v.append(list(map(int, input().split()))) for _ in range(n)]
[print(" ".join(map(str,a))) for a in sorted(v)]