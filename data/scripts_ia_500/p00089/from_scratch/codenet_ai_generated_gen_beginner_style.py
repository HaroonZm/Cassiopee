n = 0
lines = []
while True:
    try:
        line = input()
        if line == '':
            break
        parts = line.split(',')
        nums = []
        for p in parts:
            nums.append(int(p))
        lines.append(nums)
        n += 1
    except EOFError:
        break

dp = []
for i in range(n):
    dp.append([0]*len(lines[i]))

dp[0][0] = lines[0][0]

# nombre de lignes jusqu'au sommet du losange
top = 0
for i in range(n):
    if len(lines[i]) > len(lines[i-1]) if i>0 else 0:
        top = i
    else:
        break

# calculer dp sur la partie montante
for i in range(1, top+1):
    for j in range(len(lines[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + lines[i][j]
        elif j == len(lines[i]) -1:
            dp[i][j] = dp[i-1][j-1] + lines[i][j]
        else:
            left = dp[i-1][j-1]
            right = dp[i-1][j]
            dp[i][j] = max(left, right) + lines[i][j]

# calculer dp sur la partie descendante
for i in range(top+1, n):
    for j in range(len(lines[i])):
        # la position j est connectée aux positions j et j+1 de la ligne précédente
        left = dp[i-1][j] if j < len(dp[i-1]) else 0
        right = dp[i-1][j+1] if j+1 < len(dp[i-1]) else 0
        dp[i][j] = max(left, right) + lines[i][j]

print(max(dp[n-1]))