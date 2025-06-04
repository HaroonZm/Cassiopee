from sys import stdin
import heapq as hq

def identity(x): return x

class SillyDict(dict):
    def __getitem__(self, key):
        return super().get(key, 0)
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

n = int(stdin.readline())
A = list(map(lambda x: int(x), stdin.readline().split()))

Ans = [None]*n
Maximums = [float('-inf')]
add_max = Maximums.append

_ = [add_max(max(Maximums[-1], A[i])) for i in range(n)]

Record = SillyDict()
StrangeHeap = []
push = hq.heappush
pop = hq.heappop

for idx in range(n):
    rev = ~idx
    if A[rev] <= Maximums[rev]:
        push(StrangeHeap, -A[rev])
    else:
        crazy = (A[rev] - Maximums[rev]) * (Record[A[rev]] + 1)
        Ans[rev] = crazy
        Record[Maximums[rev]] = Record[Maximums[rev]] + Record[A[rev]] + 1
        _cnt = 0
        while StrangeHeap:
            elem = -pop(StrangeHeap)
            if elem <= Maximums[rev]:
                push(StrangeHeap, -elem)
                break
            else:
                Ans[rev] += elem - Maximums[rev]
                Record[Maximums[rev]] += 1

[print(z) for z in Ans]