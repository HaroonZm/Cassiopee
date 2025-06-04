import sys

def max_pond_capacity(d, w, elevation):
    max_capacity = 0
    # We need to consider every possible rectangular area of size at least 3x3
    # Iterate over all possible top-left corners
    for top in range(d):
        for left in range(w):
            # Iterate over all possible bottom-right corners with minimum size
            for bottom in range(top + 2, d):
                for right in range(left + 2, w):
                    # Extract the rectangular area boundaries
                    # Outer layer coordinates:
                    # top row: (top,left) to (top,right)
                    # bottom row: (bottom,left) to (bottom,right)
                    # left column: (top+1,left) to (bottom-1,left)
                    # right column: (top+1,right) to (bottom-1,right)
                    # Inner cells: (top+1 to bottom-1, left+1 to right-1)
                    
                    # Find elevations of outer cells and inner cells
                    outer_cells = []
                    inner_cells = []
                    
                    # Collect outer cells from top and bottom row
                    outer_cells.extend(elevation[top][left:right+1])
                    outer_cells.extend(elevation[bottom][left:right+1])
                    
                    # Collect outer cells from left and right columns (excluding corners already counted)
                    for row in range(top+1, bottom):
                        outer_cells.append(elevation[row][left])
                        outer_cells.append(elevation[row][right])
                    
                    # Collect inner cells
                    inner_cells = []
                    for row in range(top+1, bottom):
                        inner_cells.extend(elevation[row][left+1:right])
                    
                    # If there are no inner cells (should not happen due to size constraints), skip
                    if not inner_cells:
                        continue
                    
                    # The lowest elevation among the outer cells
                    min_outer = min(outer_cells)
                    
                    # Check the condition: all outermost cells strictly higher than all inner cells
                    # i.e. min outer > max inner
                    max_inner = max(inner_cells)
                    if min_outer <= max_inner:
                        continue
                    
                    # Calculate capacity: sum over inner cells of (min_outer - elevation)
                    capacity = sum(min_outer - h for h in inner_cells)
                    
                    if capacity > max_capacity:
                        max_capacity = capacity
    return max_capacity


def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        if not line:
            idx += 1
            continue
        d, w = map(int, line.split())
        if d == 0 and w == 0:
            break
        idx += 1
        elevation = []
        for _ in range(d):
            row = list(map(int, input_lines[idx].split()))
            idx += 1
            elevation.append(row)
        result = max_pond_capacity(d, w, elevation)
        print(result)

if __name__ == "__main__":
    main()