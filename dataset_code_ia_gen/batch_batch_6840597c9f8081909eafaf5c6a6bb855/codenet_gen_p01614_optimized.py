import sys
input=sys.stdin.readline

n=int(input())
phrases=[tuple(map(int,input().split())) for _ in range(n)]
m=int(input())
melodies=[int(input()) for _ in range(m)]

max_len = max(melodies)
dp = [-1]*(max_len+1)
dp[0]=0
for length in range(1, max_len+1):
    max_score = -1
    for s,l,p in phrases:
        if s <= length <= l and dp[length - length] != -1:  # length-length=0 always 0 (redundant but kept for clarity)
            max_score = max(max_score, p)
        else:
            for used_len in range(s, l+1):
                if length - used_len >=0 and dp[length - used_len]!= -1:
                    max_score = max(max_score, dp[length - used_len]+p)
    dp[length]=max_score

for w in melodies:
    print(dp[w]) if dp[w]!=-1 else print(-1) and exit()