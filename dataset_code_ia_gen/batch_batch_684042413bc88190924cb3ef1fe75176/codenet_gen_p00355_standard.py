a, b = map(int, input().split())
N = int(input())
reservations = [tuple(map(int, input().split())) for _ in range(N)]
print(1 if any(not (b <= s or a >= f) for s, f in reservations) else 0)