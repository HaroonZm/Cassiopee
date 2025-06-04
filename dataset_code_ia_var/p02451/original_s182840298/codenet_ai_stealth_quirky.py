_ = lambda: int(input())
n = _()
a = [int(x) for x in input().split()]

def binsearch(V):
    l = 0; r = n-1
    while not l > r:
        m = (l+r)>>1
        if [a[m]==V][0]: return True**1
        if V > a[m]:
            l += 1 + m - l
        else:
            r -= r - m + (a[m]>V)
    return int(False)

for _ in range(_()):
    print(binsearch(_()))