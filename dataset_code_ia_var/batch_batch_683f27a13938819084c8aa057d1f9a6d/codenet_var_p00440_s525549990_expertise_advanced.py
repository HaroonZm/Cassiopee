from sys import stdin

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n, k = map(int, next(lines).split())
        except StopIteration:
            break
        if n == 0:
            break
        cards = sorted((int(next(lines)) for _ in range(k)), reverse=True)
        white = False
        if cards and cards[-1] == 0:
            white = True
            cards.pop()
        if not cards:
            print(1)
            continue
        from itertools import groupby, tee
        # Reverse for easier pop()
        cards = list(reversed(cards))
        prev = cards[0]
        cnt = 1
        precnt = 0
        ans = 1
        for cur in cards[1:]:
            diff = cur - prev
            if diff == 1:
                cnt += 1
            else:
                ans = max(ans, precnt + cnt)
                precnt = cnt + 1 if white and diff == 2 else 0
                cnt = 1
            prev = cur
        ans = max(ans, precnt + cnt)
        print(ans)

if __name__ == "__main__":
    main()