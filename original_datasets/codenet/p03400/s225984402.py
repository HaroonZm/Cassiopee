N = int(input())
D,X = (int(i) for i in input().split())
A = [int(input()) for i in range(N)]

def count(a):
    tmp,cnt,i = 1,0,1
    while tmp <= D:
        cnt += 1
        tmp = a*i+1
        i+=1
    return cnt

cnt = 0
for a in A:
    cnt += count(a)
print(cnt+X)