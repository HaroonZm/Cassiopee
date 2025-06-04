from sys import stdin

def winner(T1, T2, R1, R2):
    if -1 in (R1, R2):
        return "Alice" if T1 < T2 else "Bob" if T1 > T2 else "Draw"
    return "Alice" if R1 > R2 else "Bob" if R1 < R2 else "Draw"

print(winner(*map(int, stdin.readline().split())))