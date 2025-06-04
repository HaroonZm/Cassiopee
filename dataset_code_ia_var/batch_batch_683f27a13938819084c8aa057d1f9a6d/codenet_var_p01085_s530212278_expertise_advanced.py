from sys import stdin

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            m, minn, maxn = map(int, next(lines).split())
            if m == minn == maxn == 0:
                break
            P = [int(next(lines)) for _ in range(m)]
            # Use max with key and enumerate for concise loop
            idx, _ = max(
                ((i, P[i] - P[i+1]) for i in range(minn-1, maxn)),
                key=lambda x: (x[1], x[0]),
                default=(0, 0)
            )
            print(idx + 1)
        except StopIteration:
            break

main()