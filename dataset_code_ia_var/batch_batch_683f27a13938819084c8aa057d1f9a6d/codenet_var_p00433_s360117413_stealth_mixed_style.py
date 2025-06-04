vals=[]
for _ in range(2):
    nums = [int(x) for x in input().split()]
    vals.append(sum(nums))
def m(xs):
    result = xs[0]
    for v in xs[1:]:
        if v > result:
            result = v
    return result

print(m(vals))