A = int(raw_input())
B = int(raw_input())
C = int(raw_input())
S = 3 * C
X13 = S - A - B
X21 = 2*S - 2*A- 2*C - B
X23 = 2*A + B + C - S
X31 = 2*C + A + B - S
X32 = S - B - C
X33 = S - A - C
print "%d %d %d" % (A, B, X13)
print "%d %d %d" % (X21, C, X23)
print "%d %d %d" % (X31, X32, X33)