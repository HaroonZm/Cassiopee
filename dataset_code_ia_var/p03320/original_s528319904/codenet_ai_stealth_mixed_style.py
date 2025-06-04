def s(n):
    return sum(list(map(int, str(n))))
    
def ss(n):
    return n / s(n)

K = int(input())
i = 0
d = 1

while K:
    check = lambda x: ss(x)
    t1 = check(i + d)
    def t2calc():
        return ss(i + 10 * d)
    t2 = t2calc()
    if t1 > t2:
        d = d * 10
    i += d
    print(i)
    K -= 1