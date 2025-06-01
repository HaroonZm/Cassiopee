import sys

lines = [list(map(int, line.strip().split(','))) for line in sys.stdin if line.strip()]
n = len(lines)
dp = [lines[0]]

for i in range(1, n):
    row = lines[i]
    prev = dp[-1]
    dp_row = []
    if i <= n//2:
        for j in range(len(row)):
            if j == 0:
                dp_row.append(prev[0] + row[0])
            elif j == len(row)-1:
                dp_row.append(prev[-1] + row[-1])
            else:
                dp_row.append(max(prev[j-1], prev[j]) + row[j])
    else:
        for j in range(len(row)):
            dp_row.append(max(prev[j], prev[j+1]) + row[j])
    dp.append(dp_row)

print(max(dp[-1]))