from sys import stdin

s = stdin.readline().strip()
n = len(s)

positions = {'1': set(), '0': set()}
for idx, c in enumerate(s):
    positions[c].add(idx)

def best_for(char):
    return min((max(i, n - i - 1) for i in positions[char]), default=n)

ansone = best_for('1')
anszero = best_for('0')

print(max(ansone, anszero))