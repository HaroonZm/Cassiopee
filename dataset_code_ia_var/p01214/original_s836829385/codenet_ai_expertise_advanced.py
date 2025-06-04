from functools import reduce, cache
from operator import or_
from typing import List

def toBinary(block: List[str]) -> List[int]:
    return [int(''.join('1' if c == '#' else '0' for c in row), 2) for row in block]

def toStr(bfield: List[int], W: int) -> List[str]:
    return [''.join('#' if (row >> i) & 1 else '.' for i in range(W-1, -1, -1)) for row in bfield]

def rotated(block: List[str]) -> List[str]:
    return [''.join(row) for row in zip(*block[::-1])]

def striped(block: List[str]) -> List[str]:
    # Remove all-dot rows from top and bottom
    block = list(block)
    dot_row = '.' * len(block[0])
    start, end = 0, len(block)
    while start < end and block[start] == dot_row:
        start += 1
    while end > start and block[end-1] == dot_row:
        end -= 1
    return block[start:end]

def canPut(x: int, y: int, w: int, h: int, W: int, H: int, bfield: List[int], bblock: List[int]) -> bool:
    if not (0 <= x <= W - w and 0 <= y <= H - h):
        return False
    shifted_block = [b << (W - w - x) for b in bblock]
    return all((f & b) == 0 for f, b in zip(bfield[y:y + h], shifted_block))

def puted(x: int, y: int, w: int, h: int, W: int, bfield: List[int], bblock: List[int]) -> List[int]:
    ret = list(bfield)
    shifted_block = [b << (W - w - x) for b in bblock]
    for i, b in enumerate(shifted_block):
        ret[y + i] |= b
    return ret

def count(bfield: List[int], W: int) -> int:
    full = (1 << W) - 1
    return sum(row == full for row in bfield)

def main():
    import sys
    input_ = iter(sys.stdin.readline, '')
    testcases = int(next(input_))
    for _ in range(testcases):
        B = list(map(int, next(input_).split()))
        block = [next(input_).rstrip() for _ in range(B[0])]
        block = striped(rotated(striped(block)))
        h, w = len(block), len(block[0])
        H, W = map(int, next(input_).split())
        field = [next(input_).rstrip() for _ in range(H)]
        bfield = toBinary(field)
        ini = count(bfield, W)
        FLAG = False
        ans = 0
        bblock = toBinary(block)
        for rot in range(4):
            for y in range(H - h + 1):
                for x in range(W - w + 1):
                    if canPut(x, y, w, h, W, H, bfield, bblock):
                        FLAG = True
                        new_bfield = puted(x, y, w, h, W, bfield, bblock)
                        new_count = count(new_bfield, W)
                        ans = max(ans, new_count)
                        if ini + max(h, w) == ans:
                            break
                if ini + max(h, w) == ans:
                    break
            block = rotated(block)
            h, w = len(block), len(block[0])
            bblock = toBinary(block)
        print(ans if FLAG else -1)

if __name__ == '__main__':
    main()