from functools import reduce

def mul(a, b): return a * b

nums = list(map(lambda x: int(x), input().split()))
if len(nums)==2:
    res = reduce(mul, nums)
    print(res)
else:
    print("Entrée invalide")