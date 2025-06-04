def read_input():
    return list(map(int, input().split()))

def is_divisible(a, b):
    return a % b == 0

def exit_with_no():
    print("No")
    quit()

def output_yes():
    print("Yes")

def initialize_S(W):
    return [0] * (W + 1)

def set_base_case(S, W, w):
    idx = W % w
    S[idx] = 1 + W // w
    return S

def fill_S(S, w, W):
    for i in range(w, W + 1):
        S[i] = S[i - w] - 1
    return S

def build_row(S, W):
    return [S[i + 1] - S[i] for i in range(W)]

def repeat_row(row, H):
    return [row[:] for _ in range(H)]

def solve(H, W, h, w):
    S = initialize_S(W)
    S = set_base_case(S, W, w)
    S = fill_S(S, w, W)
    row = build_row(S, W)
    grid = repeat_row(row, H)
    return grid

def transpose(grid):
    return [list(r) for r in zip(*grid)]

def build_grid(H, W, h, w):
    if W % w != 0:
        return solve(H, W, h, w)
    else:
        grid = solve(W, H, w, h)
        return transpose(grid)

def output_grid(grid):
    for row in grid:
        print(*row)

def main():
    H, W, h, w = read_input()
    if is_divisible(H, h) and is_divisible(W, w):
        exit_with_no()
    output_yes()
    grid = build_grid(H, W, h, w)
    output_grid(grid)

main()