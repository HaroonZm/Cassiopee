width, height = map(int, input().split())

grid = []
for _ in range(height):
    row = list(map(int, input().split()))
    grid.append(row)

# Initialize the cost table with infinity
# This 3D structure looks heavy, maybe there's a better way, but let's keep it as is for now.
costs = [[[float('inf')] * (width * height) for _ in range(height)] for __ in range(width)]
costs[0][0][0] = 0  # starting point cost

for step in range(1, width * height):
    for x in range(width):
        # if x is out of bounds for current step, break early
        if x > step:
            break
        for y in range(height):
            # likewise, if x + y exceeds step, no need to continue here
            if x + y > step:
                break

            current_cost = costs[x][y][step - 1]
            weight = (step * 2 - 1)  # simplified expression from original ((l - 1)*2 +1)

            # try moving left
            if x > 0:
                new_cost = current_cost + weight * grid[y][x - 1]
                if costs[x - 1][y][step] > new_cost:
                    costs[x - 1][y][step] = new_cost

            # try moving right
            if x < width - 1:
                new_cost = current_cost + weight * grid[y][x + 1]
                if costs[x + 1][y][step] > new_cost:
                    costs[x + 1][y][step] = new_cost

            # try moving up
            if y > 0:
                new_cost = current_cost + weight * grid[y - 1][x]
                if costs[x][y - 1][step] > new_cost:
                    costs[x][y - 1][step] = new_cost

            # try moving down
            if y < height - 1:
                new_cost = current_cost + weight * grid[y + 1][x]
                if costs[x][y + 1][step] > new_cost:
                    costs[x][y + 1][step] = new_cost

# finally find the minimum cost at bottom-right corner over all steps
result = min(costs[width - 1][height - 1])
print(result)