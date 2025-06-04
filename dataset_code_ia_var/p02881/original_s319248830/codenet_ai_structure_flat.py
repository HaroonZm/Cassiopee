import math

n = int(input())

is_prime = True
if n == 1:
    is_prime = False
else:
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            is_prime = False
            break

if is_prime:
    print(n - 1)
    exit()

ans = n
for k in range(2, int(math.sqrt(n)) + 1):
    if n % k == 0:
        temp_1 = n / k
        temp_2 = k
        if temp_1 + temp_2 < ans:
            ans = temp_1 + temp_2

print(int(ans - 2))