import sys
sys.setrecursionlimit(10**7)

# Room layout mapping each room to its adjacent rooms by direction
neighbors = {
    'A': {'N': 'D', 'E': 'B', 'S': 'E', 'W': None},
    'B': {'N': 'E', 'E': 'C', 'S': 'F', 'W': 'A'},
    'C': {'N': 'F', 'E': None, 'S': 'I', 'W': 'B'},
    'D': {'N': None, 'E': 'E', 'S': 'H', 'W': None},
    'E': {'N': 'D', 'E': 'F', 'S': 'I', 'W': 'D'},
    'F': {'N': 'E', 'E': None, 'S': None, 'W': 'E'},
    'G': {'N': 'H', 'E': None, 'S': None, 'W': None},
    'H': {'N': 'D', 'E': 'I', 'S': 'G', 'W': None},
    'I': {'N': 'F', 'E': None, 'S': None, 'W': 'H'},
}

directions = ['N', 'E', 'S', 'W']

from functools import lru_cache

def solve(n, s, t, b):

    @lru_cache(None)
    def prob(room, battery):
        if battery == 0:
            return 1.0 if room == t else 0.0
        p = 0.0
        for d in directions:
            nxt = neighbors[room][d]
            if nxt is None or nxt == b:
                nxt = room
            p += prob(nxt, battery - 1)
        return p / 4

    return prob(s, n)

for line in sys.stdin:
    line=line.strip()
    if line=='0':
        break
    n=int(line)
    s,t,b = sys.stdin.readline().split()
    print(f"{solve(n,s,t,b):.8f}")