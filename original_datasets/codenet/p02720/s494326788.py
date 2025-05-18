dic = {}
def rec(d, pre, acc):
    if d == 1:
        if 1 <= pre <= 8:
            return [acc+c for c in map(str, [pre-1, pre, pre+1])]
        elif pre == 9:
            return [acc+c for c in ["8", "9"]]
        else:
            return [acc+c for c in ["0", "1"]]
    ans = []
    for x in range(max(0,pre-1), min(pre+2, 10)):
        ans += rec(d-1, x, acc+str(x))
    return ans
K = int(input())
ls = [1,2,3,4,5,6,7,8,9]
d = 2
while len(ls) < K:
    for i in range(1,10):
        ls += rec(d-1, i, str(i))
    d+=1
print(ls[K-1])