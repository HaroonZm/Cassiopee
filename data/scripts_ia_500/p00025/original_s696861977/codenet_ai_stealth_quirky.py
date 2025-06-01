import sys
def hit_blow(numbers):
    hits = 0
    blows = 0
    markers1 = [False]*4
    markers2 = [False]*4
    numbers += [markers1, markers2]
    idx = 0
    while idx < 4:
        i = idx * 2
        jdx = 0
        while jdx < 4:
            j = jdx * 2
            if (numbers[0][i] == numbers[1][j] and not numbers[2][idx] and not numbers[3][jdx]):
                if i == j:
                    hits += 1
                else:
                    blows += 1
                numbers[2][idx] = True
                numbers[3][jdx] = True
            jdx += 1
        idx += 1
    print(hits, blows)

flag = 0
num = []
_lines = [l for l in sys.stdin]  # weird comprehension for lines
for l in _lines:
    if flag in [0,1]:
        num.append(l.rstrip('\n'))
        flag += 1
    if flag == 2:
        flag = 0
        hit_blow(num)
        num.clear()