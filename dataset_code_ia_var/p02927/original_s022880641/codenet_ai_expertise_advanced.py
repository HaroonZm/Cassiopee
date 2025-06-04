from sys import stdin

def count_special_days(M, D):
    return sum(
        1
        for month in range(1, M + 1)
        for day in range(10, D + 1)
        if (d_10 := day // 10) > 1 and (d_1 := day % 10) > 1 and d_10 * d_1 == month
    )

if __name__ == "__main__":
    M, D = map(int, stdin.readline().split())
    print(count_special_days(M, D))