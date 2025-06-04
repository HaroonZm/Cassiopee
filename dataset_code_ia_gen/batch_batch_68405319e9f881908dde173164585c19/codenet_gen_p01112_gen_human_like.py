import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        m = int(input())

        # total matches in round robin n*(n-1)//2
        total_matches = n*(n-1)//2

        # wins count per team
        wins = [0]*(n+1)

        # played matches recorded in set for quick lookup
        played = set()

        for _ in range(m):
            x, y = map(int, input().split())
            wins[x] += 1
            played.add((min(x,y), max(x,y)))

        # find remaining matches
        remain_matches = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if (i,j) not in played:
                    remain_matches.append((i,j))

        r = len(remain_matches)

        full_playoff_count = 0

        def dfs(idx):
            nonlocal full_playoff_count
            if idx == r:
                # check if all wins equal
                first = wins[1]
                for team in range(2, n+1):
                    if wins[team] != first:
                        return
                full_playoff_count += 1
                return
            a, b = remain_matches[idx]

            # team a wins
            wins[a] += 1
            dfs(idx+1)
            wins[a] -= 1

            # team b wins
            wins[b] += 1
            dfs(idx+1)
            wins[b] -= 1

        dfs(0)
        print(full_playoff_count)

if __name__ == "__main__":
    main()