pattern = [input() for _ in range(8)]

print(90)
for c in range(8):
    print(''.join(pattern[7 - r][c] for r in range(8)))
print(180)
for r in range(7, -1, -1):
    print(pattern[r][::-1])
print(270)
for c in range(7, -1, -1):
    print(''.join(pattern[r][c] for r in range(8)))