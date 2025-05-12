N = int(input())
A = [int(e) for e in input().split()]
if len(A) == len(list(set(A))):
    print('YES')
else:
    print('NO')