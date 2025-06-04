import sys

def minimal_backgammon():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        if line == '0 0 0 0':
            break
        N, T, L, B = map(int, line.split())
        idx += 1
        lose_squares = set()
        for _ in range(L):
            lose_squares.add(int(input_lines[idx]))
            idx += 1
        back_squares = set()
        for _ in range(B):
            back_squares.add(int(input_lines[idx]))
            idx += 1

        # States: positions 0..N, and whether player loses next turn or not
        # dp[t][pos][skip]: probability to be at pos at turn t with skip=0 or 1
        # skip=1 means player must skip this turn
        dp = [[[0.0,0.0] for _ in range(N+1)] for __ in range(T+1)]
        dp[0][0][0] = 1.0

        for t in range(T):
            for pos in range(N+1):
                for skip in range(2):
                    prob = dp[t][pos][skip]
                    if prob == 0.0:
                        continue
                    # If player must skip turn, then just move to next turn with skip=0, same pos
                    if skip == 1:
                        dp[t+1][pos][0] += prob
                        continue

                    # Else, roll the dice
                    for dice in range(1,7):
                        next_pos = pos + dice
                        if next_pos > N:
                            excess = next_pos - N
                            next_pos = N - excess
                        if next_pos == 0:
                            # Start square no special effect
                            dp[t+1][next_pos][0] += prob/6.0
                        elif next_pos == N:
                            # Goal square no special effect
                            dp[t+1][next_pos][0] += prob/6.0
                        elif next_pos in lose_squares:
                            # Must skip next turn
                            dp[t+1][next_pos][1] += prob/6.0
                        elif next_pos in back_squares:
                            # Sent back to start with no skip
                            dp[t+1][0][0] += prob/6.0
                        else:
                            # Normal square
                            dp[t+1][next_pos][0] += prob/6.0

        # Sum probability of being at goal in any state at any turn <= T
        ans = 0.0
        for t in range(1,T+1):
            ans += dp[t][N][0] + dp[t][N][1]
        print(f"{ans:.6f}")

if __name__ == "__main__":
    minimal_backgammon()