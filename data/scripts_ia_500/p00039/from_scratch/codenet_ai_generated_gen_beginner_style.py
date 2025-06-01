romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

import sys

for line in sys.stdin:
    s = line.strip()
    if s == "":
        continue
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and romans[s[i]] < romans[s[i+1]]:
            total += romans[s[i+1]] - romans[s[i]]
            i += 2
        else:
            total += romans[s[i]]
            i += 1
    print(total)