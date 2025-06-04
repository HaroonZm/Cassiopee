from sys import stdin
from itertools import islice

def main():
    lines = (map(int, line.split()) for line in stdin)
    it = iter(lines)
    for n, m in it:
        if n == 0:
            break
        p = list(islice(next(it), m))
        n *= not 1 in p
        print(f"{n/2:g}")

if __name__ == "__main__":
    main()