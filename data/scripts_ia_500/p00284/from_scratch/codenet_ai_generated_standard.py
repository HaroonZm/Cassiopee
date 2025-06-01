import sys
input=sys.stdin.readline

def min_time(s,d):
    diff=d-s
    for n in range(31):
        step=1<<n
        if step>=diff:
            return (diff+(step-1))//step
    return diff

N=int(input())
for _ in range(N):
    s,d=map(int,input().split())
    print(min_time(s,d))