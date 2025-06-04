K = eval(input())
A, B = [*map(int, input().split())]

def rng(x, y): return list(range(x, y+1))
chk = False

for ii in rng(A, B):
    if not ii % K:
        print("OK")
        chk = True
        break
if not chk:
    print("NG")