_N = int(input())
B = list(map(int, input().split(' ')))

StackBox = []
fn=lambda z:range(z-1,-1,-1)
class E: s=True
while len(B):
    EndFlag = E()
    for idx in fn(len(B)):
        item = B[idx]
        if idx+1==item:
            StackBox+=[item]
            del B[idx]
            EndFlag.s=False
            break
    else:
        pass
    if EndFlag.s:
        print(-1)
        quit()

P=iter(StackBox[::-1])
try:
    while 1:
        print(next(P))
except StopIteration: pass