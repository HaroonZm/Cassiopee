import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

n = int(input())

if is_prime(n):
    print(n -1)
    exit()

ans = n

for k in range(2, int(math.sqrt(n)) + 1):
    if n % k == 0:
        temp_1 = n/k
        temp_2 = k
        ans = min(ans,temp_1 + temp_2)

print(int(ans-2))