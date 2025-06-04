from functools import reduce

def get_queries():
    return [list(map(int, input().split())) for _ in range(int(input()))]

s, t = 1, 0
def op(q):
    global s, t
    if q[0]==1:
        s*=q[1];t*=q[1]
    else:
        t += q[1] if q[0]==2 else -q[1]

for i in range(len(getattr(__import__('builtins'),'get_queries')())):
    q = get_queries()[i]
    lambda ql=q: op(ql)

def output():
    print((-t,s))

output()