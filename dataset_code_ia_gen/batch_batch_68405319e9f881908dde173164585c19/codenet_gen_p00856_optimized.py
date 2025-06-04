import sys
import math

def minimal_backgammon():
    input = sys.stdin.readline
    while True:
        N, T, L, B = map(int, input().split())
        if N == 0 and T == 0 and L == 0 and B == 0:
            break
        lose = set(int(input()) for _ in range(L))
        back = set(int(input()) for _ in range(B))

        # dp[turn][pos][lost_turn_flag] = prob of being at pos with lost_turn_flag at turn-th turn
        dp = [[ [0.0,0.0] for _ in range(N+1)] for __ in range(T+1)]
        dp[0][0][0] = 1.0

        for turn in range(T):
            for pos in range(N+1):
                for lost in (0,1):
                    p = dp[turn][pos][lost]
                    if p < 1e-15:
                        continue
                    if pos == N:
                        # Already succeeded; accumulate probability at final position without change
                        dp[turn+1][pos][lost] += p
                        continue

                    if lost == 1:
                        # Lose this turn; just skip move and clear lost flag for next turn
                        dp[turn+1][pos][0] += p
                        continue

                    # Move with dice roll 1 to 6
                    prob_move = p / 6.0
                    for roll in range(1,7):
                        next_pos = pos + roll
                        if next_pos > N:
                            excess = next_pos - N
                            next_pos = N - excess
                        if next_pos == N:
                            # Reached goal
                            dp[turn+1][next_pos][0] += prob_move
                        elif next_pos in lose:
                            # Lose next turn
                            dp[turn+1][next_pos][1] += prob_move
                        elif next_pos in back:
                            # Go back to start
                            dp[turn+1][0][0] += prob_move
                        else:
                            dp[turn+1][next_pos][0] += prob_move

        ans = 0.0
        for turn in range(1, T+1):
            ans += dp[turn][N][0] + dp[turn][N][1]
        print(f"{ans:.6f}")

if __name__ == "__main__":
    minimal_backgammon()