N, D = map(int, raw_input().split())
A = map(int, raw_input().split())

g = 0
for a in A:
    g ^= (a - 1) % (D + 1)
print "First" if g else "Second"