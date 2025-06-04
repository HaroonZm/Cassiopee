N = int(input())
A = list(map(int, input().split()))

total = sum(A)
if total % 2 == 0:
    print(total // 2)
else:
    print((total - 1) // 2)