from collections import Counter
from sys import stdin

def main():
    h, w, *lines = map(str.rstrip, stdin)
    h, w = map(int, (h, w))
    freq = Counter(''.join(lines[:h]))

    counts = freq.values()
    odds = sum(v & 1 for v in counts)
    twos = sum(((v - (v & 1)) >> 1) & 1 for v in counts)

    if h % 2 == 0 and w % 2 == 0:
        res = odds == 0 and twos == 0
    elif h % 2 == 0 or w % 2 == 0:
        mid = (w if h % 2 else h) // 2
        res = odds == 0 and twos <= mid
    else:
        mid = ((h - 1) // 2) + ((w - 1) // 2)
        res = odds <= 1 and twos <= mid

    print("Yes" if res else "No")

if __name__ == "__main__":
    main()