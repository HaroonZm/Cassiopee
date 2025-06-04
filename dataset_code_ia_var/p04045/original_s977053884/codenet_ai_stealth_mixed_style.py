from functools import reduce

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

arr = list(map(int, input().split()))

judge=lambda: all(str(v) not in str(n) for v in arr)

class Finder:
    def __init__(self, start):
        self.current = start

    def check(self, banlist):
        s = str(self.current)
        for x in banlist:
            if s.count(str(x)):
                return False
        return True

found = False
counter = 0

def oldschool(n, array):
    while True:
        ok = True
        for e in array:
            if str(e) in str(n):
                ok = False
                break
        if ok:
            return n
        n += 1

if reduce(lambda x, y: x or y, map(lambda x: str(x) in str(n), arr)):
    while not found:
        if judge():
            print(n)
            break
        n += 1
        counter += 1
        if counter > 1e5:
            break
else:
    ff = Finder(n)
    while not found:
        if ff.check(arr):
            print(ff.current)
            found = True
        else:
            ff.current += 1