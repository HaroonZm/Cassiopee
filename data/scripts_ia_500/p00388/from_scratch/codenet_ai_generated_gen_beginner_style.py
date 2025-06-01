H, A, B = map(int, input().split())

count = 0
for n in range(1, H+1):
    if A * n <= H <= B * n:
        count += 1

print(count)