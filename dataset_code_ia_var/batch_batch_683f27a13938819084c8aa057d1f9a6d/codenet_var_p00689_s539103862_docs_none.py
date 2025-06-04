class Vector(tuple):
    def __neg__(self):
        return Vector([-x for x in self])
    def __abs__(self):
        return sum(x ** 2 for x in self) ** 0.5
    def __add__(self, v):
        if len(self) != len(v):
            raise ValueError("Same dimension is required.")
        return Vector([x1 + x2 for x1, x2 in zip(self, v)])
    def __sub__(self, v):
        return self.__add__(-v)
    def norm(self):
        a = self.__abs__()
        return Vector([x / a for x in self])
    def __mul__(self, v):
        if len(self) != len(v):
            raise ValueError("Same dimension is required.")
        return round(sum(x1 * x2 for x1, x2 in zip(self, v)), 14)

def main():
    while True:
        try:
            N = int(input())
        except:
            break
        if N == 0:
            break
        points = [Vector(list(map(int, input().split()))) for _ in range(N)]
        seq = [Vector([0, -1]), Vector([0, 0])]
        while len(points) != 0:
            pre = seq[-1] - seq[-2]
            points.sort(key=lambda x: abs(x - seq[-1]), reverse=True)
            points.sort(key=lambda x: (x - seq[-1]).norm() * pre.norm())
            seq += [points.pop()]
        print(round(sum(abs(v2 - v1) for v1, v2 in zip(seq[1:], seq[2:])), 1))

if __name__ == "__main__":
    main()