from sys import stdin

def generate_pattern_line(w, start_char):
    chars = ['#', '.']
    return ''.join(chars[(i + start_char) % 2] for i in range(w))

for line in stdin:
    H, W = map(int, line.split())
    if H == 0 and W == 0:
        break
    rows = [generate_pattern_line(W, shift) for shift in (0, 1)]
    print('\n'.join(rows[i % 2] for i in range(H)))
    print()