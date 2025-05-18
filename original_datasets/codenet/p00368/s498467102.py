is_ok = True
W, H = [int(i) for i in input().split()]

matrix = list()
for _ in range(H):
    matrix.append([i for i in input().split()])

up = matrix[0]
not_up = [str(int(not int(i))) for i in up]

if abs(up.count("0") * 2 - W) >= 2:
    is_ok = False

same = 1

for line in matrix[1:]:
    if up[0] == line[0]:
        same += 1
        if up != line:
            is_ok = False
            break

    elif not_up[0] == line[0] and not_up != line:
        is_ok = False
        break

if abs(same * 2 - H) >= 2:
    is_ok = False

if is_ok:
    print("yes")
else:
    print("no")