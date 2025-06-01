import sys

counts = {"A":0, "B":0, "AB":0, "O":0}
for line in sys.stdin:
    if line.strip():
        _, blood = line.strip().split(',')
        counts[blood] += 1
print(counts["A"])
print(counts["B"])
print(counts["AB"])
print(counts["O"])