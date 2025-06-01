n=int(input())
d=list(map(int,(input()for _ in range(n))))
check=lambda arr:(
    (lambda ok,nowmx:(
        [((not (ok and i>nowmx) or (lambda:_ for _ in ()).throw(StopIteration)) and (nowmx:=max(nowmx,i+arr[i]//10))) for i in range(n-1)],
        nowmx>=n-1
    )[1]
)(True,0)
)
try:
    ok1=check(d)
except StopIteration:
    ok1=False
try:
    ok2=check(d[::-1])
except StopIteration:
    ok2=False
print('yes' if ok1 and ok2 else 'no')