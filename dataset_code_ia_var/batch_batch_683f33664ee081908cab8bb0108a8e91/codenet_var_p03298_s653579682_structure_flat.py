n = int(input())
s = input()
d1 = dict()
d2 = dict()
temp1 = [None] * n
temp2 = [None] * n
for ii in range(2 ** n):
    i = ("0" * n + bin(ii)[2:])[-n:]
    cnt1 = 0
    cnt2 = n - 1
    for k, j in enumerate(i):
        if j == "1":
            temp1[cnt1] = s[k]
            temp2[cnt1] = s[2 * n - k - 1]
            cnt1 += 1
        else:
            temp1[cnt2] = s[k]
            temp2[cnt2] = s[2 * n - k - 1]
            cnt2 -= 1
    t1 = "".join(temp1)
    t2 = "".join(temp2)
    if (t1, cnt1) not in d1:
        d1[(t1, cnt1)] = 1
    else:
        d1[(t1, cnt1)] += 1
    if (t2, cnt1) not in d2:
        d2[(t2, cnt1)] = 1
    else:
        d2[(t2, cnt1)] += 1
ans = 0
for i, j in d1.items():
    if i in d2:
        ans += j * d2[i]
print(ans)