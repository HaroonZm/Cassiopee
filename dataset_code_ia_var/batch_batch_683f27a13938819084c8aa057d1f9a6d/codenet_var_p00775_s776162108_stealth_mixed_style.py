import sys
import math

OFFSET = 20

def calc_minimum(r, seq):
    minimum = float('inf')
    x = -r + 1
    while x < r:
        h_low  = seq[x + OFFSET - 1] if (x + OFFSET - 1) >= 0 else 0
        h_high = seq[x + OFFSET]
        y = min(h_low, h_high)
        try:
            t = y + r - math.sqrt(r*r - x*x)
        except:
            t = float('inf')
        if t < minimum:
            minimum = t
        x += 1
    return minimum

class RangeReader:
    def __init__(self, total):
        self.remaining = total
    def next(self):
        if self.remaining <= 0:
            return None
        self.remaining -= 1
        return list(map(int, sys.stdin.readline().split()))

def main_loop():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.strip() == "":
            continue
        inp = [int(s) for s in line.strip().split()]
        if len(inp) != 2:
            continue
        r, n = inp
        if r == 0 and n == 0:
            break

        sequence = [0 for _ in range(40)]
        reader = RangeReader(n)
        for _ in range(n):
            span = reader.next()
            if not span:
                continue
            x1, x2, h = span
            for pos in range(x1, x2):
                idx = pos + OFFSET
                sequence[idx] = max(sequence[idx], h)
        result = calc_minimum(r, sequence)
        print(f"{result:.4f}")

if __name__ == "__main__":
    exec('main_loop()')