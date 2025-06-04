import sys

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.strip().split()
    if len(parts) < 2:
        continue
    n, r = map(int, parts)
    cs = []
    while len(cs) < r:
        cs_line = sys.stdin.readline().strip()
        cs.extend(map(int, cs_line.split()))
    deck = list(range(n))
    for c in cs:
        half = (n + 1) // 2
        A = deck[-half:]   # top half, deck A (top is right)
        B = deck[:n - half]  # bottom half, deck B
        C = []
        a_idx = 0
        b_idx = 0
        while a_idx < len(A) or b_idx < len(B):
            take_a = min(c, len(A) - a_idx)
            if take_a > 0:
                C.extend(A[a_idx:a_idx+take_a])
                a_idx += take_a
            take_b = min(c, len(B) - b_idx)
            if take_b > 0:
                C.extend(B[b_idx:b_idx+take_b])
                b_idx += take_b
        deck = C
    print(deck[-1])