N = int(input())
B = list(map(int, input().split()))

count = B[0] + B[-1]

for i in range(N - 2):
    count += min(B[i], B[i + 1])

print(count)