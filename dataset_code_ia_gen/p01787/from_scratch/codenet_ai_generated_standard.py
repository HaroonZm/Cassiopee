def parse_rle():
    parts = input().split()
    rle = []
    for i in range(0, len(parts) - 1, 2):
        c = parts[i]
        l = int(parts[i+1])
        rle.append([c, l])
    return rle

def rle_to_list(rle):
    # convert RLE to list of chars (only for pattern B, which is short)
    res = []
    for c, l in rle:
        res.extend([c] * l)
    return res

def merge_rle(rle):
    if not rle:
        return []
    merged = [rle[0][:]]
    for c,l in rle[1:]:
        if c == merged[-1][0]:
            merged[-1][1] += l
        else:
            merged.append([c,l])
    return merged

A = parse_rle()
B = parse_rle()
C = parse_rle()

# Convert B to a flat string (B is the pattern to search for)
B_s = []
for c,l in B:
    B_s.extend([c]*l)
B_len = len(B_s)

# We'll implement a segment iterator for A that can give the character at any position.
# Because A's length can be very large, we only do a pointer sweep over A and try to find B_s.

# Build prefix sums of lengths of A to find positions
prefix = [0]
for c,l in A:
    prefix.append(prefix[-1]+l)
# Binary search helper
import bisect

def char_at(pos):
    # pos: 0-based index in the expanded string A
    i = bisect.bisect_right(prefix, pos)
    return A[i-1][0]

# Find first occurrence of B in A
limit = prefix[-1] - B_len + 1
found = -1
for start in range(limit):
    match = True
    for i in range(B_len):
        if char_at(start+i) != B_s[i]:
            match = False
            break
    if match:
        found = start
        break

if found == -1:
    # no occurrence, output A as is
    res = A
else:
    # Build the new string as segments without fully expanding A
    res = []
    def append_char_n(c, n):
        if n <= 0:
            return
        if res and res[-1][0] == c:
            res[-1][1] += n
        else:
            res.append([c,n])

    # prefix before found
    i = 0
    pos = 0
    while i < len(A) and prefix[i+1] <= found:
        append_char_n(A[i][0], A[i][1])
        pos += A[i][1]
        i += 1
    # partial piece before found
    if i < len(A) and pos < found:
        pre_len = found - pos
        append_char_n(A[i][0], pre_len)
        # adjust current A segment after taking pre_len
        A[i][1] -= pre_len
        pos += pre_len

    # append C
    for c,l in C:
        append_char_n(c,l)

    # skip B in A
    skip = B_len
    while i < len(A) and skip > 0:
        if A[i][1] <= skip:
            skip -= A[i][1]
            i += 1
        else:
            A[i][1] -= skip
            skip = 0
    # append the rest of A
    for j in range(i, len(A)):
        append_char_n(A[j][0], A[j][1])

    res = merge_rle(res)

for c,l in res:
    print(c, l, end=' ')
print('$')