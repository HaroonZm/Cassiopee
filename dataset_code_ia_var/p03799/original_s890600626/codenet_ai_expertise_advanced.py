from sys import stdin

def compute_ans(n: int, m: int) -> int:
    from math import floor
    if n >= m // 2:
        return m // 2
    m -= 2 * n
    return n + (m // 4)

if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    print(compute_ans(n, m))