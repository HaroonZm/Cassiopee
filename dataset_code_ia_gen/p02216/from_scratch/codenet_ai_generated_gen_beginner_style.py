n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
xor_sum = 0
for x in a:
    xor_sum ^= (x - min_a)

if xor_sum != 0:
    print("First")
else:
    if min_a % 2 == 1:
        print("First")
    else:
        print("Second")