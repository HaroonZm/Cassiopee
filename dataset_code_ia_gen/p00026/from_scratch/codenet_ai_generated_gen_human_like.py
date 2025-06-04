def main():
    # Define the grid size
    N = 10
    # Initialize the grid with zeros
    grid = [[0]*N for _ in range(N)]
    
    # Define the relative positions for each ink size
    # Including the center (0,0)
    size_offsets = {
        1: [(0,0), (1,0), (-1,0), (0,1), (0,-1)],
        2: [(0,0), (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)],
        3: [(dx,dy) for dx in range(-2,3) for dy in range(-2,3)]
    }
    
    import sys
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        # Parse input line x,y,s
        try:
            x_str,y_str,s_str=line.split(',')
            x,y,s=int(x_str),int(y_str),int(s_str)
        except:
            continue
        
        # Get affected cells
        for dx,dy in size_offsets[s]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                grid[ny][nx] += 1
                
    zero_count = sum(cell == 0 for row in grid for cell in row)
    max_density = max(cell for row in grid for cell in row)
    
    print(zero_count)
    print(max_density)

if __name__ == "__main__":
    main()