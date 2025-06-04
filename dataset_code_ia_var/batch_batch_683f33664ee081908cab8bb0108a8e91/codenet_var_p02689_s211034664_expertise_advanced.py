from sys import stdin
from operator import itemgetter

def main():
    N, M = map(int, stdin.readline().split())
    H = [0, *map(int, stdin.readline().split())]
    AB = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

    invalid = set()
    for a, b in AB:
        ha, hb = H[a], H[b]
        if ha > hb:
            invalid.add(b)
        elif ha < hb:
            invalid.add(a)
        else:
            invalid.update((a, b))
    print(N - len(invalid))

if __name__ == '__main__':
    main()