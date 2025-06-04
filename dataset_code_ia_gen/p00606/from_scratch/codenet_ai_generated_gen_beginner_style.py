import sys

# Map rooms to their neighbors (N, S, W, E)
neighbors = {
    'A': {'N': None, 'S': 'D', 'W': None, 'E': 'B'},
    'B': {'N': None, 'S': 'E', 'W': 'A', 'E': 'C'},
    'C': {'N': None, 'S': 'F', 'W': 'B', 'E': None},
    'D': {'N': 'A', 'S': 'G', 'W': None, 'E': 'E'},
    'E': {'N': 'B', 'S': 'H', 'W': 'D', 'E': 'F'},
    'F': {'N': 'C', 'S': 'I', 'W': 'E', 'E': None},
    'G': {'N': 'D', 'S': None, 'W': None, 'E': 'H'},
    'H': {'N': 'E', 'S': None, 'W': 'G', 'E': 'I'},
    'I': {'N': 'F', 'S': None, 'W': 'H', 'E': None},
}

directions = ['N', 'S', 'W', 'E']

def solve(n, s, t, b):
    memo = {}

    def dfs(room, battery):
        if battery == 0:
            if room == t:
                return 1.0
            else:
                return 0.0
        key = (room, battery)
        if key in memo:
            return memo[key]
        prob = 0.0
        for d in directions:
            nr = neighbors[room][d]
            if nr is None:
                # stay in same room
                prob += 0.25 * dfs(room, battery - 1)
            elif nr == b:
                # junk room, cannot enter, stay in same room
                prob += 0.25 * dfs(room, battery - 1)
            else:
                prob += 0.25 * dfs(nr, battery - 1)
        memo[key] = prob
        return prob

    result = dfs(s, n)
    return result

for line in sys.stdin:
    line=line.strip()
    if line == '':
        continue
    if line == '0':
        break
    n = int(line)
    line2 = sys.stdin.readline().strip()
    s,t,b = line2.split()
    ans = solve(n, s, t, b)
    print("{0:.8f}".format(ans))