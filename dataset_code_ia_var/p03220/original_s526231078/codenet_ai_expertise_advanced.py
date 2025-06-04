from typing import List

def find_closest_station(n: int, T: int, A: int, H: List[int]) -> int:
    return min(
        enumerate(H, 1),
        key=lambda x: abs(T - x[1] * 0.006 - A)
    )[0]

n = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
print(find_closest_station(n, T, A, H))