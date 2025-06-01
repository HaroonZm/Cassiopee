a, b = map(int, input().split())
N = int(input())
reservations = [tuple(map(int, input().split())) for _ in range(N)]

overlap = 0
for s, f in reservations:
    # Check if [a,b) and [s,f) overlap
    if not (b <= s or f <= a):
        overlap = 1
        break

print(overlap)