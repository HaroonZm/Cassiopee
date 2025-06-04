from sys import stdin

def solve():
    N = int(stdin.readline())
    activities = []
    idx = 0
    while idx < N:
        activities.append([int(x) for x in stdin.readline().split()])
        idx += 1
    score = [[0]*3 for _ in range(N)]
    count = 0
    while count < 3:
        score[0][count] = activities[0][count]
        count += 1

    i = 1
    while i < N:
        def update(j):
            candidates = []
            for z in range(3):
                if z != j:
                    candidates.append(score[i-1][z] + activities[i][j])
            score[i][j] = max(candidates)
        list(map(update, range(3)))
        i += 1

    res = -float('inf')
    for el in score[N-1]:
        if el > res: res = el
    print(res)

if __name__ == '__main__':
    (lambda: solve())()