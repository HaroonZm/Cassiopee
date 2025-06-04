n = int(input())
heights = [int(x) for x in input().split()]

def check(hs):
    if len(hs)==1:
        return 'Yes'
    for (idx, curr) in enumerate(hs[1:], 1):
        if hs[idx-1]<curr:
            hs[idx]=curr-1
    if all([hs[i-1]<=hs[i] for i in range(1,len(hs))]):
        return 'Yes'
    return 'No'

print(check(heights))