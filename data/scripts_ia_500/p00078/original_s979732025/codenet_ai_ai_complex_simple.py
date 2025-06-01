from functools import reduce
def magic(n):
    c,x,y=1,int(n/2),int(n/2)+1
    A=[[0]*n for _ in range(n)]
    def mod(a):return a%n
    def check(z,w):return A[z][w]==0
    def next_pos(z,w):
        return mod(z+1),mod(w+1)
    def alt_pos(z,w):
        return mod(z-1),mod(w+1)
    while True:
        A[y][x]=c
        if c==n*n:break
        while True:
            x,y=next_pos(x,y)
            if check(y,x):break
            x,y=alt_pos(x,y)
            if check(y,x):break
        c+=1
    return A
while True:
    n=reduce(lambda a,b:int(a)+int(b),list(input())) if input else int(input())
    if n==0:break
    arr=magic(n)
    _=list(map(lambda i:print(''.join(map(lambda e:format(e,'4d'),arr[i]))),range(n)))