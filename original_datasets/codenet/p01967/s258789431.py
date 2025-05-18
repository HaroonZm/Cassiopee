n = int(input())
C = list(map(int, input().split()))
q = int(input())

data = []
for _ in range(q):
    t, x, d = map(int, input().split())
    data.append([t, x, d])

apple = [0] * n
for D in data:
    t, x, d = D
    if t == 1:
        apple[x-1] += d
        if apple[x-1] > C[x-1]:
            print(x)
            break
    else:
        apple[x-1] -= d
        if apple[x-1] < 0:
            print(x)
            break
else:
    print(0)