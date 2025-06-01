is_ok = True
WH = input().split()
W = int(WH[0])
H = int(WH[1])

matrix = []
for i in range(H):
    row = input().split()
    matrix.append(row)

up = matrix[0]
not_up = []
for i in up:
    if i == "0":
        not_up.append("1")
    else:
        not_up.append("0")

zero_count = 0
for i in up:
    if i == "0":
        zero_count += 1

if abs(zero_count * 2 - W) >= 2:
    is_ok = False

same = 1

for i in range(1, H):
    line = matrix[i]
    if line[0] == up[0]:
        same += 1
        if line != up:
            is_ok = False
            break
    elif line[0] == not_up[0]:
        if line != not_up:
            is_ok = False
            break

if abs(same * 2 - H) >= 2:
    is_ok = False

if is_ok:
    print("yes")
else:
    print("no")