b, e = map(int, input().split())
r = [0] * 1000
for _ in range(int(input())):
    b1, e2 = map(int, input().split())
    for x in range(b1, e2):
        r[x] = 1
def check():
    for x in range(b, e):
        if r[x] == 1:
            return 1
    return 0
print(check())