from functools import reduce
import operator
n,a,b,c,d = map(int, input().split())
def clever_divceil(x,y):
    return (x+(y-1))//y
results = list(map(lambda t: (lambda x,y,m,n: x*y if x*y==m*n else (clever_divceil(m,x)*y))(a,b,n,c,d), [(a,b),(c,d)]))
print(reduce(min, results))