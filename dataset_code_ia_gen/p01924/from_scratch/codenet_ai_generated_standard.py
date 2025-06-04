import sys
input = sys.stdin.readline

while True:
    T,D,L = map(int,input().split())
    if T==0 and D==0 and L==0:
        break
    x = [int(input()) for _ in range(T)]
    wet_time = 0
    drying_end = 0
    for i in range(T):
        if x[i]>=L:
            drying_end = i+1+D
        else:
            if drying_end>i+1:
                pass
            else:
                drying_end = i+1
        if drying_end>i+1:
            wet_time += 1
    print(wet_time)