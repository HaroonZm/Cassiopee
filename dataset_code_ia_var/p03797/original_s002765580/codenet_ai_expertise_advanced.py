from sys import stdin

def solve_optimized():
    N, M = map(int, stdin.readline().split())
    # Calculating the maximum number of teams using advanced expressions and built-in functions
    possible_x = max(0, (M - 2 * N) // 4)
    result = min(N + possible_x, M // 2)
    print(result)

solve_optimized()