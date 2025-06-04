import sys

counts = {"A":0, "B":0, "AB":0, "O":0}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    _, blood = line.split(",")
    counts[blood] += 1

print(counts["A"])
print(counts["B"])
print(counts["AB"])
print(counts["O"])