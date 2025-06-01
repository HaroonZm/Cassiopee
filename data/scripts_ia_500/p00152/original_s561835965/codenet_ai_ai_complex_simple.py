import sys
import functools
from collections import deque
from operator import add
from itertools import tee

input = lambda: sys.stdin.readline().rstrip('\n')

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def clever_sum(*args):
    return functools.reduce(add, args, 0)

def bowling_score(data):
    n, *throws = data
    frames = deque(throws)
    frame_scores = [0]*11
    frame = 1

    def nested_fetch(n):
        nonlocal frames
        return tuple(frames[i] if i < len(frames) else 0 for i in range(n))
    
    while frame <= 10:
        head = nested_fetch(3)

        def compute_frame():
            if head[0] == 10:
                return clever_sum(*head[:3]), 1
            elif clever_sum(head[0], head[1]) == 10:
                return clever_sum(*head[:3]), 2
            else:
                return clever_sum(head[0], head[1]), 2
        
        score, consumes = compute_frame()
        for _ in range(consumes):
            frames.popleft()
        frame_scores[frame] = score
        frame +=1

    return n, sum(frame_scores[1:])

def main(_):
    while True:
        try:
            m = int(input())
        except Exception:
            break
        if not m:
            break
        results = []
        for _ in range(m):
            data = list(map(int, input().split()))
            name, score = bowling_score(data)
            results.append({"score": -score, "name": name})

        results.sort(key=lambda x: (x["score"], x["name"]))
        list(map(lambda rec: print(rec["name"], -rec["score"]), results))

if __name__ == '__main__':
    main(sys.argv[1:])