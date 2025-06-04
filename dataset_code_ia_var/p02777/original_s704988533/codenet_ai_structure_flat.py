import sys

tokens = []
for line in sys.stdin:
    tokens += line.split()

S = tokens[0]
T = tokens[1]
A = int(tokens[2])
B = int(tokens[3])
U = tokens[4]

if U == S:
    A -= 1
else:
    B -= 1

print(A, B)