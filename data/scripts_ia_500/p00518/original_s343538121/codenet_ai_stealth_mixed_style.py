import sys
from collections import Counter
from itertools import product

def solve(n, data):
    status = {(1, 0, 0): 1}
    for ch in data:
        new_status = Counter()
        for j, o, i in product([0, 1], repeat=3):
            if {'J': j, 'O': o, 'I': i}[ch]:
                for (pj, po, pi), v in status.items():
                    if (j and pj) or (o and po) or (i and pi):
                        # Utilisation d'une fonction lambda pour incrémenter
                        increment = lambda x, y: x + y
                        new_status[(j, o, i)] = increment(new_status.get((j, o, i), 0), v)
        status = {k: v % 10007 for k, v in new_status.items()}
    return sum(status.values()) % 10007

def main(*args):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().strip()
    print(solve(n, data))

if __name__ == "__main__":
    main()