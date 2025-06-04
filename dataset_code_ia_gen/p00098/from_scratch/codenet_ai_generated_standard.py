n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_sum = -10**9
for top in range(n):
    temp = [0]*n
    for bottom in range(top, n):
        for i in range(n):
            temp[i] += matrix[bottom][i]
        curr_sum = 0
        local_max = -10**9
        for val in temp:
            curr_sum = max(val, curr_sum + val)
            local_max = max(local_max, curr_sum)
        max_sum = max(max_sum, local_max)
print(max_sum)