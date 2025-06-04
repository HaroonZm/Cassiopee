n = int(input())
_S, _T = map(str, [input(), input()])
dic = {}
dic[_T[-1]] = True
idx = n - 2
while idx > 0:
    x, y = _S[idx], _T[idx]
    curr = dic[x] if x in dic else 0
    z = dic[y] if y in dic else 0
    dic[y] = (z + curr) % 1000000007
    idx -= 1
print(dic[_S[0]] if _S[0] in dic else 0)