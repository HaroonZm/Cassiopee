from bisect import bisect_left

class Score:
    __slots__ = ('t', 'score')

    def __init__(self, t):
        self.t = t
        last = [[0] for _ in range(26)]
        score = 0
        for day, contest in enumerate(t, 1):
            contest_idx = contest - 1
            score += s[day-1][contest_idx]
            last[contest_idx].append(day)
            # Optimize penalty calculation by using generator and local variables
            penalty = sum(
                c[i] * (day - last[i][-1])
                for i in range(26)
            )
            score -= penalty
            print(score)
        self.score = score

    def alternative_init(self, t):
        last = [[0] for _ in range(26)]
        score = 0
        for day, contest in enumerate(t, 1):
            idx = contest - 1
            score += s[day-1][idx]
            penalty = c[idx]*(day - last[idx][-1])
            score -= penalty
            last[idx].append(day)
            print(score)
        # Final penalty for contests not held on last days
        final_penalty = sum(
            c[i]*(D - last[i][-1])
            for i in range(26)
        )
        score -= final_penalty
        self.score = score
        self.t = t

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]

sc = Score(t)
# print(sc.score)