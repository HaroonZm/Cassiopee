import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

def full_playoff_count(n, played_matches):
    wins = [0]*n
    played = [[False]*n for _ in range(n)]
    for x,y in played_matches:
        wins[x-1]+=1
        played[x-1][y-1] = True
        played[y-1][x-1] = True
    rem_matches = []
    for i in range(n):
        for j in range(i+1,n):
            if not played[i][j]:
                rem_matches.append((i,j))
    total_rem = len(rem_matches)
    target_wins = (n-1)//2
    count = 0

    # Prune impossible branches: if a team already has wins > target_wins, no full playoff possible
    if any(w > target_wins for w in wins):
        return 0

    def dfs(idx):
        nonlocal count
        if idx == total_rem:
            if all(w==target_wins for w in wins):
                count+=1
            return
        a,b = rem_matches[idx]
        # team a wins
        wins[a]+=1
        if wins[a]<=target_wins and wins[b]<=target_wins:
            dfs(idx+1)
        wins[a]-=1
        # team b wins
        wins[b]+=1
        if wins[b]<=target_wins and wins[a]<=target_wins:
            dfs(idx+1)
        wins[b]-=1

    dfs(0)
    return count

input=sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    m=int(input())
    played_matches = [tuple(map(int,input().split())) for _ in range(m)]
    print(full_playoff_count(n, played_matches))