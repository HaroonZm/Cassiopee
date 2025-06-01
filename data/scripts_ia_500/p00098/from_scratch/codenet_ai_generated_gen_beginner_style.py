n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_sum = -10**9

for top in range(n):
    for bottom in range(top, n):
        temp = [0] * n
        for row in range(top, bottom + 1):
            for col in range(n):
                temp[col] += matrix[row][col]
        for left in range(n):
            curr_sum = 0
            for right in range(left, n):
                curr_sum += temp[right]
                if curr_sum > max_sum:
                    max_sum = curr_sum

print(max_sum)