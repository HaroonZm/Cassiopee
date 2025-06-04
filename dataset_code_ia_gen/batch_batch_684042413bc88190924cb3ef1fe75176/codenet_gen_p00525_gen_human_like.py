W, H, N = map(int, input().split())
vertical_lines = set()
horizontal_lines = set()

for _ in range(N):
    A, B, C, D = map(int, input().split())
    if A == C:  # vertical line
        vertical_lines.add(A)
    else:       # horizontal line
        horizontal_lines.add(B)

# Add the edges of the paper as boundaries
vertical_positions = [0, W] + sorted(vertical_lines)
horizontal_positions = [0, H] + sorted(horizontal_lines)

# Number of pieces = (vertical segments) * (horizontal segments)
# vertical segments = number of vertical cut lines + 1
# horizontal segments = number of horizontal cut lines + 1
result = (len(vertical_positions) - 1) * (len(horizontal_positions) - 1)
print(result)