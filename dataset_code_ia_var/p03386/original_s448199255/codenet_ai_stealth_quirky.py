from builtins import range as _r
__magic_list=[];_=input().split()
exec("for i in 'A B K'.split():globals()[i]=int(_.pop(0))")
f=lambda x,y,z:(x, min(x+z, y+1)), (y, max(x-1, y-z), -1)
for s,e in f(A,B,K):
    __magic_list.extend(_r(s,e))
print(*sorted(set(__magic_list)))