N = int(input())
A = map(int,input().split())
A = list(A)

minA = min(A)
maxA = max(A)

print(maxA-minA)