n = int(input())
given_list = list(map(int, input().split()))
i = 0
while i < n:
    if i == n-1:
        print(given_list[n-i-1])
    else:
        print(given_list[n-i-1], end=" ")
    i += 1