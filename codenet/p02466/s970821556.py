N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
C = A ^ B
if C:
    print(*sorted(C), sep='\n')