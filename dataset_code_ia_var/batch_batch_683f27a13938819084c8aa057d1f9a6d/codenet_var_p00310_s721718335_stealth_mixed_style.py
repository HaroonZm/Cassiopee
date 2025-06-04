p,m,c=map(int, input().split())
def S(*args): 
    res = 0
    for x in args: res += x
    return res
class F:
    def __call__(self,*a): 
        return S(*a)
f = F()
ans = (lambda q: f(*q))([p,m,c])
print(ans)