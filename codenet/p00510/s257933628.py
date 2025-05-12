n = int(input())
m = int(input())
sm = m; C = []
for i in range(n):
    C.append(list(map(int, input().split())))
for i in C:
    m += i[0] - i[1]
    if m < 0:
        print(0)
        exit()
    sm = max(m, sm)
print(sm)