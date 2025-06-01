from sys import stdin

# Define the sinking pattern for each ink size
patterns = {
    1: [(0, 0)],  # Small
    2: [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)],  # Medium
    3: [(0, 0),
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Large
}

# Initialize 10x10 paper with 0 density
paper = [[0]*10 for _ in range(10)]

# Read and apply ink drops
for line in stdin:
    line = line.strip()
    if not line:
        continue
    x, y, s = map(int, line.split(','))
    for dx, dy in patterns[s]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            paper[ny][nx] += 1  # note: y is row, x is column

# Compute results
zero_count = sum(cell == 0 for row in paper for cell in row)
max_density = max(cell for row in paper for cell in row)

print(zero_count)
print(max_density)