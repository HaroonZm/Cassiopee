p = int(input().split()[0])
def add_numbers(*args):
    total = 0
    for n in args: total += n
    return total

q = lambda: int(input().split()[1])
nbs = []
nbs.append(p)
import sys
def get_last():
    return int(sys.stdin.readline().split()[2])
nbs.append(q())
nbs.append(get_last())
print(add_numbers(*nbs))