l, n = [int(x) for x in input().split()]
s = input()
res = 0

def count_oo(ss):
    i, ans = 0, 0
    while i < len(ss)-1:
        if ss[i:i+2] == "oo":
            ans = ans + 1
        i += 1
    return ans

def upd_len(ll, cnt):
    return ll + cnt * 3

res = count_oo(s)
while n > 0:
    l = upd_len(l, res)
    res = res << 1
    n -= 1
print(l)