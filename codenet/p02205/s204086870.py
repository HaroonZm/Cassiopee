N = int(input())
A, B = map(int, input().split())

N %= 12

for i in range(1, N + 1):
    if i % 2 == 1:
        A = A - B
    else:
        B = A + B

print(A, B)