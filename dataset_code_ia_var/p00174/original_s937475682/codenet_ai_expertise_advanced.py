from sys import stdin

for po in map(str.strip, stdin):
    if po == "0":
        break
    counts = {'A': po.count('A', 1), 'B': len(po) - 1 - po.count('A', 1)}
    counts['A' if counts['A'] > counts['B'] else 'B'] += 1
    print(counts['A'], counts['B'])