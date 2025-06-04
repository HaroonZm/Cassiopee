import sys
input=sys.stdin.readline

while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    a=[int(input()) for _ in range(n)]
    window_sum = sum(a[:k])
    max_sum = window_sum
    for i in range(k,n):
        window_sum += a[i] - a[i-k]
        if window_sum > max_sum:
            max_sum = window_sum
    print(max_sum)