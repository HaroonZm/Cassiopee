import sys, re

pattern = re.compile(r"th(e|is|at)")
shift_char = lambda c, n: chr((ord(c) - 97 + n) % 26 + 97) if c.isalpha() else c
caesar = lambda s, n: ''.join(shift_char(ch, n) for ch in s)

for line in sys.stdin:
    line = line.lower()
    n = next(n for n in range(26) if pattern.search(caesar(line, n)))
    print(caesar(line, n).strip())