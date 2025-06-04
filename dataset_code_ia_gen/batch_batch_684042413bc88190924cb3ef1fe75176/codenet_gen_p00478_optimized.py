s = input().strip()
N = int(input())
count = 0
for _ in range(N):
    ring = input().strip()
    doubled = ring + ring
    if s in doubled:
        count += 1
print(count)