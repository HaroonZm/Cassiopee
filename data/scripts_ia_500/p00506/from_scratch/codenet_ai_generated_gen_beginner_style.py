n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if n == 2:
    g = gcd(nums[0], nums[1])
else:
    g = gcd(nums[0], gcd(nums[1], nums[2]))

divisors = []
for i in range(1, g + 1):
    if g % i == 0:
        divisors.append(i)

for d in divisors:
    print(d)