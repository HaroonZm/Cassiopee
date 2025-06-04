import sys

mapping = {
    '1': "',().-",
    '2': "abcABC",
    '3': "defDEF",
    '4': "ghiGHI",
    '5': "jklJKL",
    '6': "mnoMNO",
    '7': "pqrsPQRS",
    '8': "tuvTUV",
    '9': "wxyzWXYZ"
}

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '0':
            # count zeros
            j = i
            while j < n and s[j] == '0':
                j += 1
            zero_count = j - i
            if zero_count > 1:
                res.append(' ' * (zero_count - 1))
                i = j
            else:
                # single zero should not appear at start, and is used as separator
                # we just skip it
                i += 1
        else:
            # process group of same button digits until next zero
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            button = s[i]
            presses = j - i
            chars = mapping[button]
            length = len(chars)
            idx = (presses - 1) % length
            res.append(chars[idx])
            i = j
    print(''.join(res))