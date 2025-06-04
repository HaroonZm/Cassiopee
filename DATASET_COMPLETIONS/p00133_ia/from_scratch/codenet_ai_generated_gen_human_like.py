pattern = [list(input()) for _ in range(8)]

def rotate_90(p):
    return [''.join(p[7 - j][i] for j in range(8)) for i in range(8)]

def rotate_180(p):
    return [''.join(row[::-1]) for row in p[::-1]]

def rotate_270(p):
    return [''.join(p[j][7 - i] for j in range(8)) for i in range(8)]

r90 = rotate_90(pattern)
r180 = rotate_180(pattern)
r270 = rotate_270(pattern)

print(90)
for line in r90:
    print(line)
print(180)
for line in r180:
    print(line)
print(270)
for line in r270:
    print(line)