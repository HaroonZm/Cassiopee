import sys
sys.setrecursionlimit(10**6)
data = sys.stdin.read().split()
N = int(data[0])
A = list(map(int, data[1:]))
cache = dict()
def play(left, right, turn):
    key = (left, right, turn)
    if key in cache:
        return cache[key]
    if left == right:
        result = A[left] if N&1^turn else 0
    elif turn:
        takeL = A[left] + play((left+1)%N, right, 0)
        takeR = A[right] + play(left, (right-1)%N, 0)
        result = takeL if takeL > takeR else takeR
    else:
        res = play((left+1)%N, right, 1) if A[left] >= A[right] else play(left, (right-1)%N, 1)
        result = res
    cache[key] = result
    return result

answer = float('-inf')

def loop():
    answer = -float('inf')
    for idx in range(N):
        v = A[idx] + play((idx+1)%N, (idx-1)%N, False)
        if v > answer:
            answer = v
    return answer

print(loop())