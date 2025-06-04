from sys import stdin

def generate_pattern(H, W):
    row_even = ''.join('#.'[(col + i) % 2] for col in range(W))
    row_odd = ''.join('#.'[(col + i + 1) % 2] for col in range(W))
    for i in range(H):
        print(row_even if i % 2 == 0 else row_odd)
    print()

for line in stdin:
    H, W = map(int, line.split())
    if H == W == 0:
        break
    generate_pattern(H, W)