def largest_rectangle_in_histogram(heights):
    """
    Calculate the largest rectangle area in a histogram.
    Uses a stack-based approach for O(n) time complexity.
    """
    stack = []  # stack to keep indices of bars
    max_area = 0
    index = 0
    n = len(heights)
    
    while index < n:
        # If this bar is higher than the bar on top of stack or stack is empty, push it to stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top of the stack and calculate area
            top = stack.pop()
            # If stack is empty means everything till index has height >= heights[top]
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            if area > max_area:
                max_area = area

    # Now pop the remaining bars from stack and calculate area
    while stack:
        top = stack.pop()
        width = n if not stack else n - stack[-1] - 1
        area = heights[top] * width
        if area > max_area:
            max_area = area
    
    return max_area

def largest_rectangle_of_ones(matrix):
    """
    Given a 5x5 binary matrix, find the largest rectangular area consisting only of 1s.
    Matrix is list of lists of integers (0 or 1).
    """
    # heights array to store consecutive 1s count above (including current row)
    heights = [0] * 5
    max_rectangle = 0
    
    for row in matrix:
        # Update the heights histogram for this row
        for i in range(5):
            if row[i] == 1:
                heights[i] += 1
            else:
                heights[i] = 0
        # Calculate largest rectangle in this histogram
        area = largest_rectangle_in_histogram(heights)
        if area > max_rectangle:
            max_rectangle = area
    
    return max_rectangle


def main():
    import sys
    input = sys.stdin.read().strip('\n ')
    # Split input by lines and filter out empty lines
    lines = [line.strip() for line in input.split('\n')]
    # Remove empty lines to separate maps
    filtered_lines = [line for line in lines if line]

    m = int(filtered_lines[0])  # number of maps
    idx = 1
    results = []

    for _ in range(m):
        # Each map has 5 lines
        matrix = []
        for _ in range(5):
            row = filtered_lines[idx].split()
            idx += 1
            # Convert each element to int (0 or 1)
            matrix.append([int(x) for x in row])
        # Compute largest rectangle of 1s for the current map
        result = largest_rectangle_of_ones(matrix)
        results.append(result)
    
    # Print results for each map in separate line
    for res in results:
        print(res)

if __name__ == "__main__":
    main()