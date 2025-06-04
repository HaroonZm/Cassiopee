from sys import stdin

def best_bank():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            y = int(next(lines))
            banks = [tuple(map(int, next(lines).split())) for _ in range(n)]
            results = (
                (
                    bank[0],
                    1 + y * bank[1] / 100 if bank[2] == 1 else (1 + bank[1] / 100) ** y
                )
                for bank in banks
            )
            num_keep, _ = max(results, key=lambda x: x[1])
            print(num_keep)
        except StopIteration:
            break

best_bank()