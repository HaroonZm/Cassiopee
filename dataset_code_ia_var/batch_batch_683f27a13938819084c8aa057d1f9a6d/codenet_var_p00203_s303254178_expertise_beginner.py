import sys

def solve(field):
    queue = []
    answers = 0
    height = len(field)
    width = len(field[0])
    visited = {}

    # Add all starting positions in the first row that are 0 (blank)
    for x in range(width):
        if field[0][x] == 0:
            queue.append((x, 0))
            visited[(x, 0)] = 1

    # Loop until the queue is empty
    while queue:
        cx, cy = queue.pop(0)
        num = visited[(cx, cy)]  # Number of ways to reach here

        if field[cy][cx] == 1:
            continue  # This is an obstacle, skip

        # If we are at the last row, add to answer
        if cy == height - 1:
            answers += num
            continue

        # If this cell is a jump cell, try to jump two rows ahead
        if field[cy][cx] == 2:
            ny = cy + 2
            if ny >= height:
                answers += num
            else:
                if (cx, ny) not in visited:
                    queue.append((cx, ny))
                    visited[(cx, ny)] = 0
                visited[(cx, ny)] += num
            continue

        # Directions: down, down-left, down-right
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                # If the next cell is a jump and moving straight down
                if dx == 0 and field[ny][nx] == 2:
                    n_jump = ny + 2
                    if n_jump >= height:
                        answers += num
                    else:
                        if (nx, n_jump) not in visited:
                            queue.append((nx, n_jump))
                            visited[(nx, n_jump)] = 0
                        visited[(nx, n_jump)] += num
                elif field[ny][nx] == 0:
                    if ny == height - 1:
                        answers += num
                    else:
                        if (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited[(nx, ny)] = 0
                        visited[(nx, ny)] += num

    return answers

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        X_Y = line.strip().split()
        if len(X_Y) < 2:
            continue
        X, Y = map(int, X_Y)
        if X == 0 and Y == 0:
            break
        field = []
        for _ in range(Y):
            row = list(map(int, sys.stdin.readline().strip().split()))
            field.append(row)
        result = solve(field)
        print(result)

if __name__ == '__main__':
    main()