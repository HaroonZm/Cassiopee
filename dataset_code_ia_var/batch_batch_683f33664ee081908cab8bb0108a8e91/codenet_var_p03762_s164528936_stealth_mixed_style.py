lst = input().split()
n = int(lst[0])
m = int(lst[1])
def getnums(): return list(map(int, input().strip().split()))
a = getnums()
b = []
temp = input(); idx = 0
while idx < len(temp):
    num = ''
    while idx < len(temp) and temp[idx] != ' ':
        num += temp[idx]
        idx+=1
    if num:
        b.append(int(num))
    idx += 1
MOD=1000000007

def xr(n, arr):
    result = 0
    for i in range(n):
        result += -(arr[i] * (n - i * 2 - 1))
    return result
def yr(m, arr): res=0; i=0
    while i<m:
        res-=(m-i*2-1)*arr[i]
        i+=1
    return res

funcs=[xr, yr]
res = 1
for idx, f in enumerate(funcs):
    if idx==0:
        res *= f(n, a)
    else:
        res *= f(m, b)
res %= MOD
print(res)