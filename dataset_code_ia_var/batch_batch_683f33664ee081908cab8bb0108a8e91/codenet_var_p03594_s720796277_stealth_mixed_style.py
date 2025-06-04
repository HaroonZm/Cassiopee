from functools import reduce

H, W, d = [int(x) for x in input().split()]

palette = ['R','Y','G','B']

i = 0
while i < H:
    def cell(j):
        xi = i - j
        yj = i + j
        idx = ((xi // d) % 2) * 2 + ((yj // d) % 2)
        return palette[idx]
    # combinaison programmation fonctionnelle+impérative
    row = ""
    for j in range(W):
        row += cell(j)
    print(row)
    i += 1