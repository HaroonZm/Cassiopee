from functools import partial

def bomb(x, y, M, N=3):
    stack = [(x, y)]
    visited = set()
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        try:
            row = M[cy]
            if row[cx] != "0":
                M[cy] = row[:cx] + "0" + row[cx+1:]
                stack.extend([(cx + d, cy) for d in range(-N, 0) if d != 0] +
                             [(cx + d, cy) for d in range(1, N+1)] +
                             [(cx, cy + d) for d in range(-N, 0) if d != 0] +
                             [(cx, cy + d) for d in range(1, N+1)])
        except IndexError:
            continue

pad = 3
pad_str = "0" * pad
w, h = 14, 8
B = range(pad, pad + h)

for case in range(int(input())):
    input()
    M = [pad_str + input() + pad_str for _ in range(h)]
    M = [pad_str * w] * pad + M + [pad_str * w] * pad
    x = int(input()) + pad
    y = int(input()) + pad
    bomb(x, y, M)
    print(f"Data {case+1}:")
    for j in B:
        print(M[j][pad:-pad])