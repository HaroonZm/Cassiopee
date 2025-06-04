def decode_char(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    if '0' <= c <= '9':
        return ord(c) - ord('0') + 52
    if c == '+':
        return 62
    if c == '/':
        return 63
    return 0

def decode_line(line, length):
    bits = []
    total_bits = length
    for ch in line:
        val = decode_char(ch)
        for i in range(5, -1, -1):
            if total_bits == 0:
                break
            bits.append((val >> i) & 1)
            total_bits -=1
        if total_bits == 0:
            break
    return bits

def rotate_90(mat):
    p = len(mat)
    return [[mat[p - 1 - j][i] for j in range(p)] for i in range(p)]

def mirror(mat):
    return [row[::-1] for row in mat]

def all_transformations(pattern):
    # returns set of unique transformations (as tuple of tuples)
    result = []
    curr = pattern
    for _ in range(4):
        result.append(curr)
        result.append(mirror(curr))
        curr = rotate_90(curr)
    # unique as tuples
    unique = set()
    res = []
    for mat in result:
        tpl = tuple(tuple(row) for row in mat)
        if tpl not in unique:
            unique.add(tpl)
            res.append(mat)
    return res

import sys

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        w,h,p = map(int,line.strip().split())
        if w == 0 and h == 0 and p == 0:
            break
        
        # read image
        image_bits = []
        lines_read = 0
        while lines_read < h:
            l = sys.stdin.readline()
            if l.strip() == '':
                continue
            decoded = decode_line(l.strip(),w)
            image_bits.append(decoded)
            lines_read += 1

        # read pattern
        pattern_bits = []
        lines_read = 0
        while lines_read < p:
            l = sys.stdin.readline()
            if l.strip() == '':
                continue
            decoded = decode_line(l.strip(),p)
            pattern_bits.append(decoded)
            lines_read += 1
        
        # get all unique transformations of pattern
        patterns = all_transformations(pattern_bits)

        # preprocess patterns for quick compare: convert each to a tuple of ints
        # optional optimization: convert each pattern row to integer to compare faster
        def bit_row_to_int(row):
            v = 0
            for bit in row:
                v = (v << 1) | bit
            return v
        
        patterns_int = []
        for pat in patterns:
            pat_int = tuple(bit_row_to_int(row) for row in pat)
            patterns_int.append(pat_int)

        # also convert the image lines to integer windows for fast compare
        # Since p <= 100, we can process lines as integers
        # Prepare all horizontal windows for the image
        # For each image line, prepare prefix sums of bits as integer masks

        # we will represent each row as an integer (at most 100 bits),
        # so for each image line build an integer mask
        # but w can be up to 1000, so int of 1000 bits still okay in python
        image_int_rows = []
        for row in image_bits:
            v = 0
            for bit in row:
                v = (v << 1)|bit
            image_int_rows.append(v)
        
        count = 0
        limit_w = w - p + 1
        limit_h = h - p + 1
        # For each p\x p window in image, check if it matches any pattern transform
        # Extract the p rows from image, for columns from 0 to limit_w-1:
        # We extract bits from image_int_rows[r] at positions col to col+p-1:
        # Since bits are at leftmost = highest bit, we can shift image_int_rows[r] accordingly
        # Total bits is w, leftmost bit at pos w-1
        
        # To get bits in col..col+p-1: we shift right by (w - (col + p))
        # and mask with (1<<p)-1
        
        mask = (1 << p) -1
        for row_start in range(limit_h):
            for col_start in range(limit_w):
                # extract pattern from image lines
                window = []
                shift = w - (col_start + p)
                for r in range(row_start,row_start+p):
                    val = (image_int_rows[r] >> shift) & mask
                    window.append(val)
                window_t = tuple(window)
                # check if window match any pattern
                # only count once even if matches multiple pattern transforms
                for pat_int in patterns_int:
                    if window_t == pat_int:
                        count +=1
                        break
        print(count)

if __name__ == "__main__":
    main()