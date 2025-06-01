n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_sum = -10**9

for top in range(n):
    temp = [0] * n
    for bottom in range(top, n):
        for col in range(n):
            temp[col] += matrix[bottom][col]

        current_sum = temp[0]
        max_ending_here = temp[0]
        for k in range(1, n):
            max_ending_here = max(temp[k], max_ending_here + temp[k])
            if max_ending_here > current_sum:
                current_sum = max_ending_here

        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)