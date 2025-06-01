W, H = map(int, input().split())
paper = []
for _ in range(H):
    row = list(map(int, input().split()))
    paper.append(row)

# We can rearrange rows and columns arbitrarily, so positions can be switched.
# After rearrangement, the checkered pattern must have alternating colors:
# positions with (row + col) % 2 == 0 have the same color C,
# and positions with (row + col) % 2 == 1 have the opposite color 1 - C.
# Because we can swap rows and columns, the order of rows and columns doesn't matter,
# only the number of black squares in each parity group must match the pattern.

# Count how many squares are black in positions where (row + col) % 2 == 0 and == 1.
count_even = 0
count_odd = 0
for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            count_even += paper[i][j]
        else:
            count_odd += paper[i][j]

total_even = (H * W + 1) // 2
total_odd = (H * W) // 2

# Try color 0 for even positions and 1 for odd positions
if count_even == 0 and count_odd == total_odd:
    print("yes")
# Try color 1 for even positions and 0 for odd positions
elif count_even == total_even and count_odd == 0:
    print("yes")
else:
    # For more general check:
    # The number of black squares in even positions should be either total_even or 0
    # same for odd positions accordingly, because rows and columns can be rearranged arbitrarily.
    # Let's check if count_even equals number of black squares in even positions in any valid checkered pattern
    # That means either:
    # count_even == total_even and count_odd == 0
    # or count_even == 0 and count_odd == total_odd
    # or count_even == total_odd and count_odd == 0 (if we switch colors)
    # or count_even == 0 and count_odd == total_even
    # But total_even and total_odd are fixed, so only two patterns:
    # (black on even, white on odd) or (white on even, black on odd)
    # Let's re-check with these:
    # so either count_even == black squares count for those positions:
    # black on even = count_even == number of black squares and count_odd == 0
    # or black on odd = count_odd == number of black squares and count_even ==0
    # number of black squares total:
    black_total = sum(sum(row) for row in paper)
    # Check pattern 1: black squares == number of even positions
    if black_total == total_even and count_even == total_even and count_odd == 0:
        print("yes")
    # Check pattern 2: black squares == number of odd positions
    elif black_total == total_odd and count_even == 0 and count_odd == total_odd:
        print("yes")
    else:
        print("no")