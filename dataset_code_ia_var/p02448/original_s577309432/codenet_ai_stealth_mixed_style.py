import sys
input = sys.stdin.readline

def proc():
    n = int(input())
    data = []
    i = 0
    while i < n:
        line = input()
        s = line.strip().split()
        t = (int(s[0]), int(s[1]), s[2], int(s[3]), s[4])
        data.append(t)
        i += 1
    data = sorted(data)
    for entry in data:
        for val in entry:
            print(val, end=' ' if val != entry[-1] else '\n')
class X:
    def __call__(self): return proc()

if __name__ == "__main__":
    y = X()
    y()