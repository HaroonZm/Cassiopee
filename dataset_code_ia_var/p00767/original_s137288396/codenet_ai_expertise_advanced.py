from sys import stdin
from functools import lru_cache

def compare(h: int, w: int) -> None:
    hw = h*h + w*w

    # Generate all pairs (i, j) with i < j < 150 and store their sum of squares
    candidates = ((i, j, i*i + j*j) for j in range(2, 150) for i in range(1, j))
    
    # Find the pair (i, j) with sum of squares just larger than (h, w), with tie-breakers
    result = min(
        (i, j, ij) for i, j, ij in candidates
        if (hw < ij) or (hw == ij and h < i)
    , key=lambda x: (x[2], x[0]), default=(150, 150, 150*150 + 150*150))

    print(result[0], result[1])

def main():
    for line in stdin:
        h_w = line.strip().split()
        if len(h_w) != 2:
            continue
        h, w = map(int, h_w)
        if h == 0 and w == 0:
            continue
        compare(h, w)

if __name__ == "__main__":
    main()