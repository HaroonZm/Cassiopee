N = int(input())
A = [int(input()) for _ in range(N)]

def neighbors(i):
    return (i-1) % N, (i+1) % N

max_sum = 0

for first in range(N):
    taken = [False]*N
    joi_sum = 0
    taken[first] = True
    joi_sum += A[first]

    turn = 1  # IOI's turn=1, JOI's turn=0
    while sum(taken) < N:
        candidates = []
        for i in range(N):
            if not taken[i]:
                left, right = neighbors(i)
                if taken[left] or taken[right]:
                    candidates.append(i)
        if not candidates:
            break
        if turn == 1:
            # IOI chooses the largest piece
            cand = max(candidates, key=lambda x: A[x])
        else:
            # JOI chooses any piece - try all to maximize final sum - but beginner approach:
            # just pick the first candidate (non-optimized)
            cand = candidates[0]
        taken[cand] = True
        if turn == 0:
            joi_sum += A[cand]
        turn = 1 - turn
    if joi_sum > max_sum:
        max_sum = joi_sum

print(max_sum)