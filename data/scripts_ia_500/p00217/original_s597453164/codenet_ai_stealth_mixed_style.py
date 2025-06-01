import sys
class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __cmp__(self, other):
        return other.y - self.y
def solve(n):
    a = []
    for i in xrange(n):
        line = raw_input()
        nums = line.split()
        vals = map(int, nums)
        temp_pair = Pair(vals[0], vals[1]+vals[2])
        a.append(temp_pair)
    a.sort()
    print a[-1].x, a[-1].y
def main():
    from sys import stderr
    while True:
        ipt = raw_input()
        if ipt.isdigit():
            n = int(ipt)
            if not n:
                break
            solve(n)
        else:
            stderr.write(ipt)
if __name__=="__main__":
    main()