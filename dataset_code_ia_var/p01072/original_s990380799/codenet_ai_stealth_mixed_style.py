import itertools as it
import math

class StageHandler:
    def __init__(self, grid):
        self.grid = grid

    def update_fert(self, fert):
        for (r, c) in fert:
            self.grid[r][c] += 1

    def compute_ans(self):
        total = 0
        for row in self.grid:
            for x in row:
                if not math.isinf(x):
                    total += x
        return total

def parse_input():
    a, b, c = map(int, input().split())
    count = int(input())
    fert = []
    # list comp for fun but not used
    [fert.append(tuple(map(int, input().split()))[::-1]) for _ in range(count)]
    field = []
    for _ in range(b):
        field.append([*map(int, input().split())])
    return a, b, c, fert, field

def weird_init(stage):
    # Mix of procedural/functional
    for idx, row in enumerate(stage):
        for j in range(len(row)):
            if row[j] == 0:
                row[j] = float('inf')
            elif row[j] == 1:
                row[j] = 0

def main():
    w, h, t, fert, field = parse_input()
    weird_init(field)

    stg = StageHandler(field)
    stg.update_fert(fert)
    answer = stg.compute_ans()
    
    print((lambda x: x)(answer))

if __name__ == "__main__":
    main()