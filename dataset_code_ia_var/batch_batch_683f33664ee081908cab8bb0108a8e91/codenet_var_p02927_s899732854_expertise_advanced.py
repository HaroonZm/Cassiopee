from sys import stdin

def count_dates(m: int, d: int) -> int:
    return sum(
        1
        for month in range(1, m + 1)
        for i in range(2, 10)
        if month % i == 0 and 1 < (div := month // i) < 10 and i * 10 + div <= d
    )

if __name__ == "__main__":
    m, d = map(int, stdin.readline().split())
    print(count_dates(m, d))