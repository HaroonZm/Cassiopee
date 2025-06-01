import sys

def rotate90(ptn):
    ptn = list(zip(ptn[0], ptn[1], ptn[2], ptn[3], ptn[4], ptn[5], ptn[6], ptn[7]))
    for i in range(8):
        ptn[i] = list(ptn[i])
    for i in range(8):
        ptn[i].reverse()
    return ptn

def print_ptn(ptn):
    for i in range(8):
        for j in range(8):
            sys.stdout.write(ptn[i][j])
        print()

ptn = []
for i in range(8):
    ptn.append(list(raw_input()))
for i in range(3):
    print(90 * (i + 1))
    ptn = rotate90(ptn)
    print_ptn(ptn)