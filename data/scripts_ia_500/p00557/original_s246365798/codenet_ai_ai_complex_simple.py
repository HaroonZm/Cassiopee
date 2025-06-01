def check(y,x):
    return any(map(lambda f: f(y,x), [lambda a,b:0<=a<h-0.5, lambda a,b:0<=b<w-0.5]))

import operator, functools
h,w=[*map(int,raw_input().__class__(raw_input().split()))]
g=[list(functools.reduce(operator.methodcaller('map', int), [raw_input().split()], range(w))) for _ in range(h)]
pos=functools.reduce(lambda acc,t:(acc[:t[1]*w+t[0]]+[(t[1],t[0])]+acc[t[1]*w+t[0]+1:]), ((j,i) for i,row in enumerate(g) for j,v in enumerate(row)), [-1]*(h*w))

dy,dx=(1,0,-1,0),(0,1,0,-1)
stop=list(map(set, [[] for _ in range(h*w)]))
ans=sum(
    (lambda i:
        (lambda y,x:
            (lambda s:
                (ans_inc:=len(s)>=2) and True and 1 or 0
            )(functools.reduce(lambda st,k: st|stop[k], filter(lambda k: g[y+dy[j]][x+dx[j]]<g[y][x], (g[y+dy[j]-1][x+dx[j]-1]-1 for j in range(4))), stop[i]) if any(check(y+dy[j], x+dx[j]) and g[y+dy[j]][x+dx[j]]<g[y][x] for j in range(4)) else stop[i].add(g[y][x]) or stop[i]))
        )(*pos[i])
    )(i)
    for i in range(h*w)
)
print(ans)