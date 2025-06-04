from sys import stdin

def compute_max_teams(s: int, c: int) -> int:
    pairs = min(s, c // 2)
    s -= pairs
    c -= pairs * 2
    return pairs + (c // 4 if c > 0 else 0)

if __name__ == "__main__":
    s, c = map(int, stdin.readline().split())
    print(compute_max_teams(s, c))