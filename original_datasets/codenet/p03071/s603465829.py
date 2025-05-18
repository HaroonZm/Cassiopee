A, B=map(int,input().split())
print(max(A, B)+max(max(A, B)-1, min(A,B)))