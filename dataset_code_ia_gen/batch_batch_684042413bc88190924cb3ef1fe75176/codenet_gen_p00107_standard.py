import math
while True:
    A,B,C = map(int,input().split())
    if A==0 and B==0 and C==0:
        break
    n=int(input())
    d = math.sqrt(A*A + B*B + C*C)
    for _ in range(n):
        R = int(input())
        print("OK" if 2*R >= d else "NA")