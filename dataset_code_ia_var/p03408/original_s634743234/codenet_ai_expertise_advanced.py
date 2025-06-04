from collections import Counter
import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    it = iter(input_lines)
    n = int(next(it))
    c1 = Counter(next(it) for _ in range(n))
    m = int(next(it))
    c2 = Counter(next(it) for _ in range(m))
    result = max((v - c2[k] for k, v in c1.items()), default=0)
    print(max(0, result))

if __name__ == "__main__":
    main()