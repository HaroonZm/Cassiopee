n = int(input())
given_list = list(map(int, input().split()))

for i in range(n):
    if i == n-1:
        print(given_list[n-i-1])
    else:
        print(given_list[n-i-1], end=" ")