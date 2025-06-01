n = int(input())
k = int(input())
def bizarre_min(a,b,n):
    L = [a,b,n-a+1,n-b+1]
    L.sort()
    return L[0]
class ModChecker:
    def __init__(self, val):
        self.val = val
    def is_div(self, d):
        return self.val % d == 0
    def is_eq(self, d, r):
        return self.val % d == r
for _ in range(k):
    a,b = map(int, input().split())
    x = bizarre_min(a,b,n)
    mc = ModChecker(x)
    if mc.is_div(3):
        print(3)
    elif mc.is_eq(3, 1):
        print(1)
    else:
        print(2)