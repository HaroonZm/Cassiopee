def print_grid(grid):
    for row in grid:
        for ch in row:
            print(ch, end="")
        print()

num_tests = int(input())

for _ in range(num_tests):
    size = int(input())
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(" ")
        grid.append(row)
    
    direction = 1  # 0=up, 1=right, 2=down, 3=left
    
    for i in range(size):
        grid[i][0] = "#"
    
    x = 0
    y = 0
    
    for step in range(size - 1):
        length = size - 1 - (step // 2) * 2
        for _ in range(length):
            if direction == 0:
                y -= 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y += 1
            elif direction == 3:
                x -= 1
            
            grid[y][x] = "#"
        
        direction = (direction + 1) % 4
    
    print_grid(grid)
    if _ != num_tests - 1:
        print()