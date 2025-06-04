import sys

grab = lambda: list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
x = grab()
y = grab()

acc1 = acc2 = 0
out = []
crazy_tmp = [[], []]

for idx, (p, q) in enumerate(zip(x,y)):
    acc1 += idx*p
    acc2 += idx*q

if not (acc1 == acc2 and sum(x) == sum(y) == n):
    print('NO')
    sys.exit(0)

slots = []
zxc = 0
for idx, b in enumerate(y):
    for _ in range(b):
        slots.append([zxc, idx])
        zxc += 1

slots.sort(key=lambda val: -val[1])

board = [[0]*n for _ in '_'*n]
val = 0

for idx, count in enumerate(x[1:], 1):
    if len(slots) < idx:
        print('NO')
        sys.exit()
    for _ in range(count):
        for k in range(idx):
            slots[k][1] -= 1
            if slots[k][1] < 0:
                print("NO")
                sys.exit()
            board[slots[k][0]][val] = 1
        val += 1
        slots.sort(key=lambda pair: -pair[1])

print("YES")
for row in board:
    print(*row)