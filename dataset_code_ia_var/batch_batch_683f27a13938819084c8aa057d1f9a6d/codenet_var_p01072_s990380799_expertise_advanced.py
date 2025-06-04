import sys
from itertools import product
import numpy as np

def main():
    w, h, t = map(int, sys.stdin.readline().split())
    p = int(sys.stdin.readline())
    fert_coords = [tuple(map(int, sys.stdin.readline().split()))[:2][::-1] for _ in range(p)]
    stage = np.array([list(map(int, sys.stdin.readline().split())) for _ in range(h)], dtype=float)
    mask_0 = (stage == 0)
    mask_1 = (stage == 1)
    stage[mask_0] = float('inf')
    stage[mask_1] = 0
    for r, c in fert_coords:
        stage[r, c] += 1
    print(int(np.isfinite(stage).sum() and np.nansum(np.where(np.isfinite(stage), stage, 0))))

if __name__ == '__main__':
    main()