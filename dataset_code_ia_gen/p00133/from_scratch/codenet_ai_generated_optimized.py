grid = [input() for _ in range(8)]

def rotate90(g):
    return [''.join(g[7 - j][i] for j in range(8)) for i in range(8)]

r90 = rotate90(grid)
r180 = rotate90(r90)
r270 = rotate90(r180)

print(90)
print(*r90, sep='\n')
print(180)
print(*r180, sep='\n')
print(270)
print(*r270, sep='\n')