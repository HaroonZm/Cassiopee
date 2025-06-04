from heapq import heappush, heappop

def main():
    """
    Main function to process the map based on surrounding influences.
    Simulates "cascade" processing on a map filled with integers and dots ('.'),
    where '.' cells are filled and cause adjacent numbered cells to decrease,
    propagating the effect until possible.
    Finally prints the number of turns required for the last fill.
    """
    # Read the height and width of the map from user input
    h, w = map(int, input().split())

    # Build the map with a border of -1s to simplify boundary checks
    # Convert input lines to lists, padding each row with -1 on left and right
    mp = [[-1] + list(input()) + [-1] for _ in range(h)]
    # Add a top and bottom border of -1s to the map
    mp.insert(0, [-1] * (w + 2))
    mp.append([-1] * (w + 2))

    # Priority queue for cells to process; stores tuples (turn, x, y)
    que = []

    # Initialize the map and queue:
    #   - Convert numbered cells from str to int
    #   - For each '.' cell, set value to 0 and push into the queue as ready to process
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if "1" <= mp[y][x] <= "9":
                mp[y][x] = int(mp[y][x])
            elif mp[y][x] == ".":
                mp[y][x] = 0
                heappush(que, (0, x, y))

    # 8 directions for adjacency: right, left, down-right, down, down-left, up-right, up, up-left
    vec = (
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, 0),  # up
        (-1, -1)  # up-left
    )

    # Process queue
    # For each cell taken from the queue, try to lower adjacent numbered cells by 1
    # If any such cell drops to 0, push it into the queue for the next turn
    while que:
        turn, x, y = heappop(que)
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] > 0:  # Only process numbered cells above zero
                mp[ny][nx] -= 1
                if mp[ny][nx] == 0:
                    heappush(que, (turn + 1, nx, ny))

    # After processing all, the last 'turn' processed corresponds to the required number of turns
    print(turn)

main()