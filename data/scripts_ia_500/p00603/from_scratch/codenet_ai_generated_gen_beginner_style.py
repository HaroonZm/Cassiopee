import sys

for line in sys.stdin:
    if line.strip() == "":
        continue
    parts = line.strip().split()
    if len(parts) < 2:
        continue
    n = int(parts[0])
    r = int(parts[1])
    operations = []
    while len(operations) < r:
        ops_line = sys.stdin.readline()
        ops_parts = ops_line.strip().split()
        for op in ops_parts:
            if len(operations) < r:
                operations.append(int(op))
    # Initialize deck: bottom to top is from 0 to n-1
    deck = list(range(n))
    for c in operations:
        # split deck into two halves A and B
        mid = (n + 1) // 2
        A = deck[mid:]
        B = deck[:mid]
        # deck A is the top half, which is deck[mid:] since right is top
        # deck B is the bottom half, deck[:mid]
        deck_C = []
        while A or B:
            take_A = min(c, len(A))
            for _ in range(take_A):
                deck_C.append(A.pop())
            take_B = min(c, len(B))
            for _ in range(take_B):
                deck_C.append(B.pop())
        deck = deck_C
    # top card is the last element in deck
    print(deck[-1])