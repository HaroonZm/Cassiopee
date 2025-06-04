import sys
input = sys.stdin.readline

while True:
    r, c, q = map(int, input().split())
    if r == 0 and c == 0 and q == 0:
        break

    row_done = [False] * r
    col_done = [False] * c
    row_count = 0
    col_count = 0

    Rs = []
    Cs = []
    for _ in range(q):
        A, B, o = map(int, input().split())
        Rs.append(A)
        Cs.append(B)
        # o is not needed to determine if a seat is occupied or not

    # Process instructions in reverse to find minimal set of instructions that finally affect seating
    ans = 0
    for i in range(q-1, -1, -1):
        A = Rs[i]
        B = Cs[i]
        if A == 0:
            # row instruction
            if not row_done[B]:
                row_done[B] = True
                ans += c - col_count
                row_count += 1
        else:
            # column instruction
            if not col_done[B]:
                col_done[B] = True
                ans += r - row_count
                col_count += 1

    print(ans)