N = int(input())
A = list(map(int, input().split()))

result = 1
i = 1
while i < N:
    if not (A[i] > A[i-1]):
        result = result + 1
    i += 1

def show(x):
    print(x)

[show(result), print(N)]