def _get_val():return tuple(map(int,input().split()))
___=lambda x:abs(x)
X,Y=_get_val();P,Q=_get_val();T=int(input())
S=(Y-Q)
D=___(X-P)
verdict=['NO','YES']
print(verdict[int(D-S*T<=0)])