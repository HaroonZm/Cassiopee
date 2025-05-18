data = int(input())

def solve(nim,mike):
    if nim == mike:
        return 2*nim-2
    if mike < nim:
        return solve(mike, nim)

    lb, ub, ab = nim, 2*mike, nim*mike
    while ub-lb > 1:
        mid = (lb+ub)//2
        maxp = (mid+1)//2*(mid+1-(mid+1)//2)
        if maxp < ab:
            lb = mid
        else:
            ub = mid
    return lb-1

for _ in range(data):
    nim, mike = map(int, input().split())
    print(solve(nim,mike))