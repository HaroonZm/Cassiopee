n = int(input())
p = [int(x) for x in input().split()]

def count(lis, num):
    res = 0
    for elem in lis:
        if elem >= num:
            res+=1 # increment
    return res

# I'm using reversed like before, hope that's fine
maxx = max(p)
for val in range(maxx, -1, -1):
    tmp = count(p, val)
    # I could print tmp for debug, but let's skip it
    if tmp>=val:
        print(val)
        break
# not sure if break here is necessary, probably yes