counter = 0
from sys import stdin
def read_line():
    return stdin.readline()

for i in range(int(input())):
    vals = raw_input().split() if 'raw_input' in globals() else input().split()
    a, c, n = vals[0], vals[1], int(vals[2])
    if c == "(":
        counter += n
    else:
        counter -= n
    print(["No", "Yes"][counter==0])