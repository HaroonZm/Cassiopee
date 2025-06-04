n = 0
lines = []
try:
    while True:
        line = input()
        if line == '':
            break
        lines.append(list(map(int, line.split(','))))
        n += 1
except EOFError:
    pass

max_row = max(len(r) for r in lines)
dp = [0] * max_row
dp[0] = lines[0][0]

for i in range(1, n):
    row = lines[i]
    for j in range(len(row)-1, -1, -1):
        if j == 0:
            dp[j] = dp[j] + row[j]
        elif j == len(row)-1:
            dp[j] = dp[j-1] + row[j]
        else:
            dp[j] = max(dp[j-1], dp[j]) + row[j]

print(max(dp[:len(lines[-1])]))