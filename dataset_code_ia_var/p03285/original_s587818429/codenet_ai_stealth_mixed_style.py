n = int(input())
def check(n):
    from functools import reduce
    result = list()
    for i in range(25):
        for j in range(14):
            if 4*i+7*j==n:
                result.append((i,j))
    return len(result)

count = check(n)
if not count:
    print('No')
else:
    print('Yes')