import sys

def next_char(c):
    return chr((ord(c)-ord('A')+1)%26 + ord('A'))

def prev_char(c):
    return chr((ord(c)-ord('A')-1)%26 + ord('A'))

def decode_letter(s, i):
    # Returns (decoded_char, next_index)
    # s[i] can be '+', '-', 'A'-'Z', or '?'
    cnt_plus = 0
    cnt_minus = 0
    while i < len(s) and s[i] in '+-':
        if s[i] == '+': cnt_plus += 1
        else: cnt_minus += 1
        i += 1
    c = s[i]
    i += 1
    if c == '?':
        # Need to find letter that results in lex smallest
        # Because increments and decrements are fixed, we try A..Z letters and take minimal resulting char
        candidates = []
        for base_ord in range(ord('A'), ord('Z')+1):
            c0 = chr(base_ord)
            c1 = c0
            # apply plus
            for _ in range(cnt_plus):
                c1 = next_char(c1)
            for _ in range(cnt_minus):
                c1 = prev_char(c1)
            candidates.append((c1, c0))
        candidates.sort(key=lambda x: x[0])
        return candidates[0][0], i
    else:
        c1 = c
        for _ in range(cnt_plus):
            c1 = next_char(c1)
        for _ in range(cnt_minus):
            c1 = prev_char(c1)
        return c1, i

def parse_cipher(s, i=0):
    # Returns (decoded_string, next_index)
    res = []
    while i < len(s):
        if s[i] == ']':
            # End of current cipher
            break
        elif s[i] == '[':
            # parse inside and reverse
            i += 1
            inside, i = parse_cipher(s, i)
            if i >= len(s) or s[i] != ']':
                # syntax error but problem doesn't require to check
                pass
            i += 1
            res.append(inside[::-1])
        else:
            c, i = decode_letter(s, i)
            res.append(c)
    return ''.join(res), i

for line in sys.stdin:
    line = line.strip()
    if line == '.':
        break
    decoded, _ = parse_cipher(line, 0)
    print(decoded)