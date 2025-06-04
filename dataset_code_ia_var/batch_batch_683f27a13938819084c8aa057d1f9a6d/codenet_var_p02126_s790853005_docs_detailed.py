def main():
    """
    Reads input values, processes a list of items (balls), and selects up to M items based on certain constraints and priorities.
    Each ball has a color and weight, and allocation is limited by total capacity for each color and overall item count.

    The function prints the maximal sum of selected weights under the constraints.
    """
    # Read the number of balls (N), total items to select (M), and number of colors (C)
    N, M, C = map(int, input().split())

    # Read the initial availability/count for each color (L: list of length C)
    *L, = map(int, input().split())

    # Read the list of balls. Each ball is represented as a pair (color, weight).
    BALL = [list(map(int, input().split())) for _ in range(N)]

    # Sort the balls in descending order of weight
    BALL.sort(key=lambda x: x[1], reverse=True)

    ans = 0  # This will accumulate the total weight of selected balls

    # Iterate over each sorted ball, trying to select as per the constraints
    for c, w in BALL:
        # Check if there is still capacity for this color
        if L[c-1]:
            ans += w        # Select this ball: add its weight
            L[c-1] -= 1     # Decrease available slots for this color
            M -= 1          # Decrease the overall number of items to pick
            if M == 0:
                break       # Stop if reached the total requested items

    # Output the final total weight
    print(ans)

if __name__ == "__main__":
    main()