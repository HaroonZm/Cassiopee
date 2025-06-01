import sys

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Note: This cmp thing is kinda old school but whatever
    def __cmp__(self, other):
        return self.y - other.y  # sorts by y ascending

def solve(n):
    pairs = []
    for _ in range(n):
        line = raw_input()
        parts = line.split()
        nums = map(int, parts)  # assuming exactly 3 ints per line
        p = Pair(nums[0], nums[1] + nums[2])  # sum of 2nd and 3rd numbers
        pairs.append(p)
    pairs.sort()
    # the last element has the biggest y after sorting ascending
    biggest = pairs[-1]
    print biggest.x, biggest.y

def main():
    while True:
        inp = raw_input()
        if inp.isdigit():
            n = int(inp)
            if n == 0:
                break
            solve(n)
        else:
            # weird input? just dump it to stderr
            sys.stderr.write(inp + "\n")

if __name__ == "__main__":
    main()