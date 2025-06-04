def dist(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        dp[i][0] = i
    for j in range(len2+1):
        dp[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            cost = 0 if s1[i-1]==s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,    # delete
                           dp[i][j-1]+1,    # insert
                           dp[i-1][j-1]+cost) # replace or same
            if i>1 and j>1 and s1[i-1]==s2[j-2] and s1[i-2]==s2[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-2][j-2]+1) # swap adjacent
    return dp[len1][len2]

while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    d = int(input())
    names = [input() for _ in range(n)]
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            distance = dist(names[i], names[j])
            if distance <= d:
                a,b = sorted([names[i], names[j]])
                pairs.append((a,b))
    pairs.sort()
    for p in pairs:
        print(p[0]+','+p[1])
    print(len(pairs))