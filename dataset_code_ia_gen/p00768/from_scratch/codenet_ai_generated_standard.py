import sys

def main():
    input = sys.stdin.readline
    while True:
        M, T, P, R = map(int, input().split())
        if M == 0 and T == 0 and P == 0 and R == 0:
            break
        solved = [[False]*P for _ in range(T)]
        wrong = [[0]*P for _ in range(T)]
        time_solved = [[0]*P for _ in range(T)]
        for _ in range(R):
            m, t, p, j = map(int, input().split())
            t -= 1
            p -= 1
            if solved[t][p]:
                continue
            if j == 0:
                solved[t][p] = True
                time_solved[t][p] = m + 20*wrong[t][p]
            else:
                wrong[t][p] += 1
        teams = []
        for i in range(T):
            count = sum(solved[i])
            total_time = sum(time_solved[i])
            teams.append((count, total_time, i+1))
        teams.sort(key=lambda x:(-x[0], x[1], x[2]))
        res = []
        i = 0
        while i < T:
            j = i+1
            group = [teams[i][2]]
            while j < T and teams[j][0] == teams[i][0] and teams[j][1] == teams[i][1]:
                group.append(teams[j][2])
                j += 1
            group.sort(reverse=True)
            res.append("=".join(map(str, group)))
            i = j
        print(",".join(res))

if __name__ == "__main__":
    main()