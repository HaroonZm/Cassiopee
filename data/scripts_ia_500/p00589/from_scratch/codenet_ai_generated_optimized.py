import sys

mapping = {
    '1': " '(),-.",
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
    line = line.strip()
    if not line:
        continue
    result = []
    i = 0
    n = len(line)
    while i < n:
        c = line[i]
        if c == '0':
            count0 = 1
            i += 1
            while i < n and line[i] == '0':
                count0 += 1
                i += 1
            if count0 > 1:
                result.append(' ' * (count0 - 1))
            # if count0 == 1 and first char is not zero (input never starts with zero), 
            # single zero acts as separator only, so output nothing
        else:
            count = 1
            j = i + 1
            while j < n and line[j] == c:
                count += 1
                j += 1
            # Determine cycle length
            chars = mapping[c]
            cycle = len(chars)
            index = (count - 1) % cycle
            result.append(chars[index])
            i = j
            continue
        i += 1
    print(''.join(result))