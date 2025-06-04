from sys import stdin
from collections import defaultdict
import bisect

def main():
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    q = int(stdin.readline())
    
    pos = defaultdict(list)
    for idx, val in enumerate(A):
        pos[val].append(idx)
    
    for _ in range(q):
        a, b, c = map(int, stdin.readline().split())
        indices = pos.get(c, [])
        left = bisect.bisect_left(indices, a)
        right = bisect.bisect_left(indices, b)
        print(right - left)

if __name__ == "__main__":
    main()