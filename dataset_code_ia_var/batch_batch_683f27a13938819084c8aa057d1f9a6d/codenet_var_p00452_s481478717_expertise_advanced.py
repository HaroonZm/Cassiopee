from itertools import combinations_with_replacement
from bisect import bisect_right

def input_score(n):
    return [0, *map(int, (input() for _ in range(n)))]

def cal_two_sum_score(score):
    s = set()
    for a in score:
        for b in score:
            s.add(a + b)
    return sorted(s)

def cal_four_sum_score(two_score, m):
    max_score = 0
    for t in two_score:
        idx = bisect_right(two_score, m - t) - 1
        if idx >= 0:
            sum_score = t + two_score[idx]
            if sum_score <= m:
                max_score = max(max_score, sum_score)
                if max_score == m:
                    break
    return max_score

def main():
    import sys
    input_iter = iter(sys.stdin.read().splitlines())
    while True:
        try:
            N, M = map(int, next(input_iter).split())
        except StopIteration:
            break
        if N == 0 and M == 0:
            break
        score = input_score(N)
        two_score = cal_two_sum_score(score)
        max_score = cal_four_sum_score(two_score, M)
        print(max_score)

if __name__ == "__main__":
    main()