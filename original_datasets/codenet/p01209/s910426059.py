import string
INF = 1 << 30

def conv(base, num):
    ret = 0
    for n in str(num):
        if n in string.ascii_letters:
            n = ord(n) - ord("A") + 10
        else:
            n = int(n)
        ret = ret * base + n
    return ret

def get_fact(n):
    ret = []
    for i in xrange(2, n + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
        if cnt != 0:
            ret.append((i, cnt))
    return ret

while True:
    base, num = raw_input().split()
    if (base, num) == ("0", "0"):
        break
    base = int(base)
    num = conv(base, num)
    fact = get_fact(base)
    ans = [] #tmp
    for f,n in fact:
        ff = f
        cnt = 0
        while ff <= num:
            cnt += num / ff
            ff *= f
        ans.append(cnt / n)
    print min(ans)