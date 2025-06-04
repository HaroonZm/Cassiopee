from sys import stdin

def main():
    lines = iter(stdin)
    while True:
        try:
            m, n_min, n_max = map(int, next(lines).split())
        except StopIteration:
            break
        if m == 0:
            break
        v = [int(next(lines)) for _ in range(m)]
        idx_gap = (
            max(
                ((i, v[i-1] - v[i]) for i in range(n_min, n_max+1)),
                key=lambda x: (x[1], x[0])
            )[0]
        )
        print(idx_gap)

if __name__ == "__main__":
    main()