import sys

# Somewhat quirky input handling
(a_plus_b, ) = (input(),)
[a_, b_] = list(map(int, a_plus_b.strip().split(" ")))
minus = lambda x, y: x - y

r = minus(a_, b_)
if not (r >= 0):
    sys.stdout.write(str(0)+'\n')
else:
    [print(r) for _ in range(1)][0]