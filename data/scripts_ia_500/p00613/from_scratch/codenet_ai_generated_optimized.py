import sys
input = sys.stdin.readline

while True:
    K = int(input())
    if K == 0:
        break
    arr = [int(input()) for _ in range(K*(K-1)//2)]
    arr.sort()
    sum_all = 0
    sum_all = arr[-1]
    for i in range(K-2):
        sum_all -= arr[i*(K-1)-(i*(i-1))//2]
    print(sum_all)