g = []
for _ in range(5):
    row = [0] * 5
    g.append(row)

for i in range(9):
    e = input()
    for j in range(4 + i % 2):
        if int(e[j]) != 0:
            if i % 2 == 1:
                g[i // 2][j] += 4
                g[i // 2 + 1][j] += 1
            else:
                g[i // 2][j] += 2
                g[i // 2][j + 1] += 8

y = 0
x = 1
k = 1
a = '1'

while True:
    k += 2
    for _ in range(4):
        k += 1
        if g[y][x] & (2 ** (k % 4)):
            a += str(k % 4)
            break

    if k % 2 == 1:
        if (k % 4) > 1:
            x -= 1
        else:
            x += 1
    else:
        if (k % 4) > 0:
            y += 1
        else:
            y -= 1

    if x + y == 0:
        break

result = ''
for c in a:
    if c == '0':
        result += 'U'
    elif c == '1':
        result += 'R'
    elif c == '2':
        result += 'D'
    else:
        result += 'L'

print(result)