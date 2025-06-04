import sys

get_input=lambda:sys.stdin.readline().strip()
def intinput(): return int(get_input())
def mapinput(): return map(int, get_input().split())
def listinput(n=None): return list(mapinput()) if n is None else [intinput() for _ in range(n)]

def matrix2d(row,col,fill): return [[fill]*col for _ in range(row)]
matrix3d = lambda x, y, z, v: [[[v]*z for _ in range(y)] for _ in range(x)]
def list4(x, y, z, k, val):
    return [[[[val for _ in range(k)] for _ in range(z)] for _ in range(y)] for _ in range(x)]

sys.setrecursionlimit(10**9)
INF=10**19; MOD=10**9+7; EPS=1e-10

def yes():print('Yes')
def no():print('No')
YES_=lambda:print('YES')
NO_=lambda:print('NO')

def roundup(x, y=1): return (x+y-1)//y

D=intinput()
C=listinput()
S=[]
for idx in range(D):
    tmp=[int(x) for x in get_input().split()]
    S.append(tmp)
T=[t-1 for t in listinput(D)]
M=26
last = matrix2d(M, D+2, 0)

def compute_score(selection):
    ans=0
    for day, t in enumerate(selection):
        ans+=S[day][t]
        for j in range(M): last[j][day+1]=last[j][day]+1
        last[t][day+1]=0
        for j in range(M): ans -= C[j]*last[j][day+1]
    return ans

def eval_change(day,a,b):
    next_a=last[a].index(0,day+2)
    width=next_a-day-1
    high=last[a][day]+1
    penalty_a = C[a]*high*width
    for d in range(day,next_a-1):
        last[a][d+1]=last[a][d]+1

    next_b=last[b].index(0,day+2)
    width_b=next_b-day-1
    high_b=last[b][day]+1
    penalty_b=C[b]*high_b*width_b
    last[b][day+1]=0
    i=day+1
    while i<next_b-1:
        last[b][i+1]=last[b][i]+1
        i+=1
    result = -penalty_a + penalty_b - S[day][a] + S[day][b]
    return result

current_score = compute_score(T)
Q = intinput()
for request in range(Q):
    arr=tuple(mapinput())
    d=arr[0]-1;q=arr[1]-1
    prev=T[d];nxt=q
    current_score+=eval_change(d,prev,nxt)
    print(current_score)
    T[d]=q