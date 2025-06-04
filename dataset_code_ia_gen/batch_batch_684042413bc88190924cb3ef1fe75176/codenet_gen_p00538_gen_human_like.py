import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

# 0-based index for convenience
# Since pieces are arranged in a circle, neighbors are (i-1)%N and (i+1)%N

# We try all possible first picks by JOI-kun
max_sum = 0

for first in range(N):
    taken = [False]*N
    joi_sum = A[first]
    taken[first] = True
    # The order of picking after the first pick is:
    # IOI first, then JOI, alternating
    
    # We maintain a list of pieces still available
    # and pick according to rules:
    # A piece can be taken if at least one neighbor is taken
    
    # After the first pick, the candidates are neighbors of first pick (both not taken)
    # On each turn:
    # - IOI must take the largest piece among candidates
    # - JOI can pick any from candidates
    
    # We simulate picking until all pieces are taken
    
    # We'll keep track of candidates for next pick (pieces adjacent to taken pieces)
    taken_count = 1
    
    # Using a deque or set to find candidates easily
    candidates = set()
    for i in range(N):
        if not taken[i]:
            # check if either neighbor is taken
            left = (i-1)%N
            right = (i+1)%N
            if taken[left] or taken[right]:
                candidates.add(i)
    
    turn_ioi = True  # IOI picks next
    
    # For JOI's picks, he wants to maximize sum,
    # so he will choose the candidate with largest A[i]
    
    while taken_count < N:
        if turn_ioi:
            # IOI chooses the largest piece among candidates
            if not candidates:
                break
            pick = max(candidates, key=lambda x:A[x])
            taken[pick] = True
            candidates.remove(pick)
        else:
            # JOI chooses optimally: pick candidate with largest A[i]
            if not candidates:
                break
            pick = max(candidates, key=lambda x:A[x])
            taken[pick] = True
            candidates.remove(pick)
            joi_sum += A[pick]
        taken_count += 1
        
        # update candidates: new candidates are pieces not taken
        # and have at least one neighbor taken
        for i in range(N):
            if not taken[i]:
                left = (i-1)%N
                right = (i+1)%N
                if taken[left] or taken[right]:
                    candidates.add(i)
                else:
                    candidates.discard(i)
        turn_ioi = not turn_ioi
    
    max_sum = max(max_sum, joi_sum)

print(max_sum)