import sys
sys.setrecursionlimit(10**7)

def solve_chain(chars):
    from collections import deque

    def eliminate(line):
        changed = True
        while changed:
            changed = False
            nline = []
            i = 0
            while i < len(line):
                j = i
                while j < len(line) and line[j][0] == line[i][0]:
                    j += 1
                length = j - i
                if length >= 4:
                    changed = True
                else:
                    nline.extend(line[i:j])
                i = j
            line = nline
        return line

    N = len(chars)
    res = N

    colors = [1,2,3]
    for i in range(N):
        orig_color = chars[i][0]
        for c in colors:
            if c == orig_color:
                continue
            # Change color at i
            new_line = chars[:i] + [(c,1)] + chars[i+1:]
            # Merge adjacent same colors counts for the changed position neighbors
            # First reconstruct run-length encoding
            rle = []
            for col, cnt in new_line:
                if rle and rle[-1][0] == col:
                    rle[-1] = (col, rle[-1][1] + cnt)
                else:
                    rle.append((col, cnt))
            # After color change, we merge runs accordingly:
            # But here new_line is already run-length encoded per char with count=1
            # So to be efficient, let's reconstruct the full list of chars:
            full_line = []
            for col, cnt in rle:
                full_line.extend([col]*cnt)
            # Convert to run-length with counts:
            rle2 = []
            i2 = 0
            while i2 < len(full_line):
                j2 = i2
                while j2 < len(full_line) and full_line[j2] == full_line[i2]:
                    j2 += 1
                rle2.append((full_line[i2], j2 - i2))
                i2 = j2
            # Eliminate continuously
            eliminated = eliminate(rle2)
            length = sum(c for _, c in eliminated)
            if length < res:
                res = length
    return res

input=sys.stdin.readline

while True:
    N = int(input())
    if N==0:
        break
    chars = []
    for _ in range(N):
        c = int(input())
        chars.append((c,1))
    print(solve_chain(chars))