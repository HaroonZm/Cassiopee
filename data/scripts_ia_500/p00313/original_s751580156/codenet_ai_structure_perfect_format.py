n = int(input())
V = [0]*n
for i in [1, 2, 4]:
    for e in map(int, input().split()[1:]):
        V[e-1] += i
print(sum((e & 4 > 0) and (e != 5) for e in V))