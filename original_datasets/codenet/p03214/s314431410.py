n = int(input())
a = list(map(int, input().split()))

ave = sum(a) / n
ret = 0
hoge = 1e9

for i in range(n):
    tmp = abs(ave - a[i])
    if  tmp < hoge:
        ret = i
        hoge = tmp

print(ret)