b, e = map(int, input().split())
r = []
for i in range(1000):
    r.append(0)

n = int(input())
for i in range(n):
    b1, e2 = map(int, input().split())
    for x in range(b1, e2):
        r[x] = 1

def check():
    for x in range(b, e):
        if r[x] == 1:
            return 1
    return 0

print(check())