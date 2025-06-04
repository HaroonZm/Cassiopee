from sys import exit
from functools import reduce

coords = tuple(map(int, input().split()))
if all(map(lambda x: x == 0, coords)):
    print("1")
    exit()

F=lambda n: reduce(lambda a,_: a+[a[-1]+a[-2]], range(n-2), [0,1])
R=[[0,0],[0,0]]
T=[(lambda n: (n%4==2 or n%4==3),lambda n: (n%4==0 or n%4==1))]

for i in (lambda: iter(int,1))():
    f=F(i+1)[-1]
    [(lambda t: R[t][i%2].__iadd__(f) if t else R[t][i%2].__isub__(f))(k(i)) for t,k in enumerate(T)]
    bounds = [R[0][0]<=coords[0]<=R[1][0], R[0][1]<=coords[1]<=R[1][1]]
    if all(bounds):
        print(((i-1)%3)+1)
        break