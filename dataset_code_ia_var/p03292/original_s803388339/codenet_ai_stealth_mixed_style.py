from functools import reduce

def get_vals():
    return [int(x) for x in input().split()]

arr = sorted(get_vals())

res = 0
for i,y in enumerate(arr[1:]):
    res += abs(y - arr[i])

print(res)