from math import isqrt

def count_valid_pairs(M: int, D: int) -> int:
    return sum(
        1
        for j in range(22, D + 1)
        if (tens := j // 10) >= 2 and (units := j % 10) >= 2
        and (prod := tens * units) <= M and prod == (i := prod)
    )

if __name__ == "__main__":
    M, D = map(int, input().split())
    print(count_valid_pairs(M, D))