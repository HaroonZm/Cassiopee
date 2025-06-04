from sys import stdin
from statistics import mean

def process_scores():
    results = []
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            scores = [int(next(lines)) for _ in range(n)]
            trimmed_scores = scores.copy()
            trimmed_scores.remove(max(trimmed_scores))
            trimmed_scores.remove(min(trimmed_scores))
            results.append(sum(trimmed_scores) // (n - 2))
        except StopIteration:
            break
    print(*results, sep='\n')

if __name__ == '__main__':
    process_scores()