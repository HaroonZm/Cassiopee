import sys
import re

def shift_char(match, n):
    char = match.group(0)
    return chr((ord(char) - 97 + n) % 26 + 97)

def cipher(line, n):
    return re.sub(r"\w", lambda x: shift_char(x, n), line)

for line in sys.stdin:
    n = 0
    translated = cipher(line, n)
    while not re.search(r"th(e|is|at)", translated):
        n += 1
        translated = cipher(line, n)
    print(translated.strip())