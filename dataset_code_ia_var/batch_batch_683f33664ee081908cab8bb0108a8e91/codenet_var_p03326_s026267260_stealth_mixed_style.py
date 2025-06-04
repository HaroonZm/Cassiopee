from numpy import array, sort, sum as npsum

def getNM():
    n, m = map(int, input().split())
    return n, m

def getPoints(n):
    res = [[] for _ in range(3)]
    for _ in range(n):
        line = input().split()
        for idx, val in enumerate(line):
            res[idx].append(int(val))
    return tuple(array(r) for r in res)

class XYZCombinator:
    def __init__(self, x, y, z):
        self.arrs = [x, y, z]

    def build(self):
        ops = [
            (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
            (-1, -1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1)
        ]
        v = []
        for o in ops:
            combined = o[0] * self.arrs[0] + o[1] * self.arrs[1] + o[2] * self.arrs[2]
            v.append(combined)
        return v

def takeTopSum(arr, m):
    return npsum(sort(arr)[::-1][:m])

if __name__ == '__main__':
    N, M = getNM()             # Procedural
    x, y, z = getPoints(N)     # Functional
    xyz = XYZCombinator(x, y, z).build()   # OOP
    score = [takeTopSum(arr, M) for arr in xyz]   # List Comprehension
    print(max(score))          # Script/block style