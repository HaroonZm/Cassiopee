def q(x):return raw_input(x) if x else raw_input()
def p(*a):print ' '.join(map(str,a))
class R(dict):
    def __getitem__(s,k):return dict.get(s,k,-1)
ninja = lambda u: int(''.join(sorted(str(u[0]).zfill(u[1]))[::-1]))-int(''.join(sorted(str(u[0]).zfill(u[1]))))
while 1:
    t=q("").split();A,G=int(t[0]),int(t[1])
    if (A|G)==0:break
    J,cnt=R(),-1
    while True:
        J[A]=cnt=cnt+1
        A=ninja((A,G))
        if J[A]!=-1:
            p(J[A],A,cnt-J[A])
            break