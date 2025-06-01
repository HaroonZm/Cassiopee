from functools import reduce
a,b,c=map(int,input().split())
def step(state):
    i,c=state
    c-=a
    if i%7==0:
        c-=b
    return (i+1,c)
i,c=1,c
while True:
    i,c=step((i,c))
    if c<=0:
        break
print(i)