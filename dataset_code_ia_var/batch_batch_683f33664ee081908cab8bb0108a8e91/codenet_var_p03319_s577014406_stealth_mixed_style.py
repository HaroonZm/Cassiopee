nums = input().split()
n = int(nums[0])
k = int(nums[1])
a = [int(j) for j in input().split()]
def process(n, k):
    n = n - k
    k = k - 1
    if n <= 0:
        return 1
    else:
        from math import ceil
        return 1 + (n // k) if n % k == 0 else 2 + (n // k)
result = (lambda x, y: process(x, y))(n, k)
print(result)