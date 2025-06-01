from sys import stdin
weights = (1, 9, 36, 84, 126)
for line in stdin:
    digits1 = map(int, line[:5])
    digits2 = map(int, reversed(line[5:10]))
    print(sum(w * (d1 + d2) for w, d1, d2 in zip(weights, digits1, digits2)) % 10)