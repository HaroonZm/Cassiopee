def main():
    """
    Main function to solve the shortest path problem described.
    Given a board of N squares (with some blocked), determine the sequence
    of dice rolls (1-M per move) that moves a player from start to finish in
    the smallest number of moves, ensuring lexicographically smallest for ties.
    Greedy approach is applied backward from the goal.
    """
    # Read two integers, N (number of spaces) and M (max dice value per move)
    N, M = map(int, input().split())
    # Read the string S (path) and reverse it (so goal is S[0], start S[N])
    S = input()[::-1]

    # List to store moves made (in reverse order, from goal backward)
    ans = []
    # Current position; start from the goal (position 0)
    now = 0

    while True:
        # Check if we can reach or exceed the start in one move
        if now + M >= N:
            # Add the final step that brings us to the start and terminate
            ans.append(N - now)
            break

        # Try to make the largest possible move (M steps forward)
        step = M
        # If destination square is blocked, decrement step size greedily
        while S[now + step] == '1':
            step -= 1
            # If no possible moves remain, the path is blocked
            if step == 0:
                print(-1)
                return

        # Move to the next position
        now += step
        # Record the step size taken
        ans.append(step)

    # Output the sequence of moves, in correct order from start to finish
    print(*ans[::-1])

if __name__ == "__main__":
    main()