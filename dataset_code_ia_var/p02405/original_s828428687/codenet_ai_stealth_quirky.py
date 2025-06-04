def get_dim():
    z=lambda:map(int,input().split())
    return z()

def draw(h,w):
    s=['#','.']
    k=''
    for i in range(h):
        for j in range(w):
            k+=s[(i^j)&1]
        k+='\n'
    return k

exec("a,b=get_dim()\nwhile(a|b):print(draw(a,b));a,b=get_dim()")