from sys import exit as leave,stdout
MILLION = 10**6
parse = lambda x: map(int, x.split())
numb = lambda : raw_input().strip()
N,M= parse(numb())
if M==1:
    x=0b1
    for _ in range(N): x=(x<<1)%MILLION
    print x
    leave()
buf = [[0]*3 for _ in range(N+2)]
buf[0][:] = [1,0,0]
buf[1][:] = [1]*3
jazz = range(N+2)
s = lambda arr: reduce(lambda x,y: (x+y)%MILLION, arr, 0)
for k in jazz[1:]:
    buf[k][1]=s(buf[k-1])
    buf[k][0]=(s(buf[k-1]) + s([buf[t][2] for t in jazz[:k-1]]))%MILLION
    buf[k][2]=(s(buf[k-1]) + s([buf[t][0] for t in jazz[:k-1]]))%MILLION
print buf[N+1][2]