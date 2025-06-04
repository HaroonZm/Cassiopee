r, s, p = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(p)]

# Create the car layout: rows x (2*s + 1)
# The aisle is at position s (0-based), seats 0..s-1 on left, s+1..2s on right
width = 2 * s + 1
car = [[None for _ in range(width)] for _ in range(r)]

# Place passengers
for idx, (i, j) in enumerate(positions):
    # Convert to 0-based indices, seat positions shifted by -1
    car[i-1][j-1] = idx

steps = 0
passengers_left = p

while passengers_left > 0:
    moved = [False]*p
    new_car = [row[:] for row in car]

    # Step 1: Try passengers in seats move towards aisle or into aisle
    # Fill moves for passengers on seats, from front row to back and from left to right
    for i in range(r):
        for j in range(width):
            pid = car[i][j]
            if pid is not None and not moved[pid]:
                # If on aisle already
                if j == s:
                    continue
                # If next position towards aisle is empty
                if j < s:
                    next_j = j + 1
                else:
                    next_j = j - 1
                if car[i][next_j] is None and new_car[i][next_j] is None:
                    new_car[i][next_j] = pid
                    new_car[i][j] = None
                    moved[pid] = True

    car = [row[:] for row in new_car]

    # Step 2: Move passengers in aisle row backward if possible or exit
    # Process from back to front, so that back passengers move first
    for i in range(r-1, -1, -1):
        pid = car[i][s]
        if pid is not None and not moved[pid]:
            # If at rear row, passenger gets off
            if i == r-1:
                new_car[i][s] = None
                moved[pid] = True
                passengers_left -= 1
            else:
                # Move backward if the position is free or will be free
                if car[i+1][s] is None and new_car[i+1][s] is None:
                    new_car[i+1][s] = pid
                    new_car[i][s] = None
                    moved[pid] = True

    car = [row[:] for row in new_car]

    steps += 1

print(steps)