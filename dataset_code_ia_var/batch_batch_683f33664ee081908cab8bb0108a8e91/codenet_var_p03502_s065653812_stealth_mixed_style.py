def y(): return input().strip()
ss = y()
N = int(ss)
NN = sum(map(int, (lambda x: list(x))(ss)))
if N % NN == 0:
    res = "Yes"
else:
    res = "No"
print(res)