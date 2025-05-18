# coding=utf-8

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    qtype, b, e = map(int, input().split())
    if qtype == 0:
        print(min(A[b:e]))
    elif qtype == 1:
        print(max(A[b:e]))