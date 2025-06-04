h, w = (lambda: list(map(int, input().split())))()
p = [input() for _ in range(h)]

make_matrix = lambda fill: [[fill]*w for _ in " "*h]
r = make_matrix('.')
b = make_matrix('.')

for idx in range(h):
    # first/last cols
    r[idx][0] = '#'
    b[idx][-1] = '#'
    middle = range(1, w-1)
    for col in middle:        
        (r if idx%2==0 else b)[idx][col] = '#'

# Handling obstacles
for i in range(1, h-1):
    for j in range(1, w-1):
        if p[i][j]=='#':
            r[i][j]=b[i][j]="#"

[print(*row, sep='') for row in r]
print()
list(map(lambda line: print(''.join(line)), b))