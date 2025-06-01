import math

A = [i+1 for i in range(30)]
B = [int(input()) for i in range(28)]

diff = sorted(list(set(A)-set(B)))

print(diff[0])
print(diff[1])