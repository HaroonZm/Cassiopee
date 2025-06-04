import math

def get_ints(s): return list(map(int, s.split()))

def create_map():
    return dict((i, 0) for i in range(-50, 50))

class Process:
    def __init__(self):
        self.result = 100
        self.heights = create_map()
    def update(self, x1, x2, h):
        for j in range(x1, x2):
            if self.heights[j] < h:
                self.heights[j] = h
    def compute_min(self, r):
        for i in range(-r, 0):
            s = r - math.sqrt(r * r - (i + 1) * (i + 1)) + self.heights[i]
            self.result = s if s < self.result else self.result
        i = 0
        while i < r:
            s = r - math.sqrt(r * r - i * i) + self.heights[i]
            if s < self.result:
                self.result = s
            i += 1
        return self.result

def read_input():
    try:
        while True:
            tmp = raw_input()
            vals = get_ints(tmp)
            if not vals: continue
            r, n = vals
            if r == 0: break
            proc = Process()
            for __ in range(n):
                args = get_ints(raw_input())
                proc.update(*args)
            print proc.compute_min(r)
    except EOFError:
        pass

if __name__ == '__main__':
    read_input()