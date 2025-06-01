import sys

INF = 10 ** 18
MOD = 10 ** 9 + 7

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    ls = []
    a = map(int, sys.stdin.readline().split())
    for num in a:
        ls.append(num * 2)
    b = map(int, sys.stdin.readline().split())
    for num in b:
        ls.append(num * 2 + 1)
    ls.sort(reverse=True)
    cnt1 = cnt2 = 0
    ans = "NA"
    for num in ls:
        if num % 2 == 1:
            cnt2 += 1
        else:
            cnt1 += 1
            if (cnt1 - cnt2) * 2 > cnt1 and cnt1 != N:
                ans = cnt1
                break
    print(ans)