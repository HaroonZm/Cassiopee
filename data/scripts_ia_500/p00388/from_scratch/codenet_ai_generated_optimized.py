H,A,B = map(int, input().split())
count = 0
min_n = (H + B - 1) // B  # smallest number of floors
max_n = H // A            # largest number of floors
if min_n <= max_n:
    count = max_n - min_n + 1
print(count)