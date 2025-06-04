from sys import stdin

def decide_winner(t1, t2, r1, r2):
    match (r1, r2):
        case (-1, _) | (_, -1):
            match (t1 - t2):
                case x if x < 0: return "Alice"
                case x if x > 0: return "Bob"
                case _: return "Draw"
        case _:
            match (r1 - r2):
                case x if x > 0: return "Alice"
                case x if x < 0: return "Bob"
                case _: return "Draw"

print(decide_winner(*map(int, stdin.readline().split())))