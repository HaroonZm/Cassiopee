class Twelvefold:
    def __init__(Inst, N, MODULUS):
        Inst.m = MODULUS
        Inst.F = [1] + [0]*N
        for _i in range(1,N+1):
            Inst.F[_i]=Inst.F[_i-1]*_i%MODULUS
        Inst.I = [1]*(N+1)
        Inst.I[N] = pow(Inst.F[N],MODULUS-2,MODULUS)
        for IR in range(N,0,-1): Inst.I[IR-1] = Inst.I[IR]*IR%MODULUS
        def zero2d():
            return [[0]*(N+1) for _ in range(N+1)]
        Inst.S,Inst.B,Inst.P = zero2d(),zero2d(),zero2d()
        Inst.S[0][0]=Inst.B[0][0]=1
        for ROW in range(N):
            for COL in range(N):
                v = Inst.S[ROW][COL+1]
                v2 = Inst.S[ROW][COL]
                Inst.S[ROW+1][COL+1]=(v2+(COL+1)*v)%MODULUS
        for R in range(N):
            for C in range(N):
                Inst.B[R+1][C+1]=(Inst.B[R+1][C]+Inst.S[R+1][C+1])%MODULUS
        for J in range(N): Inst.P[0][J]=1
        for I in range(N):
            for J in range(N):
                if I-J>=0:
                    Inst.P[I+1][J+1]=(Inst.P[I+1][J]+Inst.P[I-J][J+1])%MODULUS
                else:
                    Inst.P[I+1][J+1]=Inst.P[I+1][J]%MODULUS

    def solve(self,*args,**kwargs):
        n,k=args[0],args[1]
        a,b = kwargs.get('equate_element',False), kwargs.get('equate_subset',False)
        c,d = kwargs.get('less_than_1',False), kwargs.get('more_than_1',False)
        assert not (c and d)
        _id = a*3 + b*6 + c + d*2
        call = [
            self.one,self.two,self.three,self.four,self.five,self.six,
            self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve
        ]
        return call[_id](n,k)

    def one(self,a,b): return pow(b,a,self.m)
    def two(me,x,y): return 0 if y-x<0 else me.F[y]*me.I[y-x]%me.m
    def three(m,n,k): return m.S[n][k]*m.F[k]%m.m
    def four(this,n,k):
        if not k: return 0
        return this.F[n+k-1]*this.I[n]*this.I[k-1]%this.m
    def five(obj,n,k):
        if k-n<0: return 0
        return obj.F[k]*obj.I[n]*obj.I[k-n]%obj.m
    def six(o,n,k):
        if n-k<0 or k==0: return 0
        x= o.F[n-1]*o.I[k-1]%o.m
        return x*o.I[n-k]%o.m
    seven = lambda s,n,k: s.B[n][k]
    eight = lambda f,n,k: 0 if k-n<0 else 1
    nine = lambda s,n,k: s.S[n][k]
    ten = lambda t,n,k: t.P[n][k]
    eleven = lambda z,n,k: 0 if k-n<0 else 1
    def twelve(self,n,k):
        if n-k<0: return 0
        return self.P[n-k][k]

a,b=map(int,input().split())
TF = Twelvefold(1000,10**9+7)
print(TF.solve(a,b,equate_element=0,equate_subset=0,less_than_1=0,more_than_1=0))