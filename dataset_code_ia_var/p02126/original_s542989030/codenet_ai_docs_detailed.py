def read_input():
    """
    Reads initial problem parameters and the available quantity of each color.
    
    Returns:
        N (int): Number of balls available in total.
        M (int): Number of balls that must be selected.
        C (int): Number of different colors.
        colors (list of int): List where colors[i] is the number of balls available for color i+1.
    """
    N, M, C = map(int, input().split())
    colors = [int(l) for l in input().split()]
    return N, M, C, colors

def read_balls(N):
    """
    Reads information about each individual ball.
    
    Args:
        N (int): Number of balls to be read.
    Returns:
        ball (list of [int, int]): Each element is [color, value] for each ball.
    """
    ball = []
    for _ in range(N):
        c, w = map(int, input().split())
        ball.append([c, w])
    return ball

def select_balls(N, M, colors, ball):
    """
    Selects up to M balls with maximum total value while obeying color limits.
    
    The selection process gives preference to balls with higher value, and for each ball,
    it checks if a ball of its color is still available. If yes, selects it, reduces
    the available color count, and accumulates its value toward the total cost.
    
    Args:
        N (int): Number of balls available.
        M (int): Number of balls required to be selected.
        colors (list of int): List of available ball counts for each color.
        ball (list of [int, int]): List of balls, each with a color and value.

    Returns:
        cost (int): The maximum possible total value of the selected balls.
    """
    # Sort the balls descendingly by value (ball[i][1])
    ball.sort(key=lambda x: x[1])
    ball.reverse()
    
    take = 0              # Number of balls taken so far
    cost = 0              # Total value of the balls selected
    i = 0                 # Current index in the sorted ball list

    while (take <= M - 1) and (i <= N - 1):
        # Check if there are balls left for the color of the current ball
        if colors[ball[i][0] - 1] == 0:
            i += 1
            continue    # Skip if no balls left for this color
        else:
            cost += ball[i][1]                          # Add the value of the chosen ball
            colors[ball[i][0] - 1] -= 1                 # Decrease available count for the color
            take += 1                                   # Increment the number of balls taken
            i += 1                                      # Move to the next ball in the list

    return cost

def main():
    """
    Main function to read input, process data, and print the result.
    """
    N, M, C, colors = read_input()
    ball = read_balls(N)
    result = select_balls(N, M, colors, ball)
    print(result)
    
if __name__ == "__main__":
    main()