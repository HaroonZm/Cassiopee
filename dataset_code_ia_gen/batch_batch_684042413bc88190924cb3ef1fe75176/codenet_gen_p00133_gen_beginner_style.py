pattern = []
for _ in range(8):
    line = input()
    pattern.append(line)

# 90度回転
print(90)
for i in range(8):
    new_line = ""
    for j in range(7, -1, -1):
        new_line += pattern[j][i]
    print(new_line)

# 180度回転
print(180)
for i in range(7, -1, -1):
    new_line = ""
    for j in range(7, -1, -1):
        new_line += pattern[i][j]
    print(new_line)

# 270度回転
print(270)
for i in range(7, -1, -1):
    new_line = ""
    for j in range(8):
        new_line += pattern[j][i]
    print(new_line)