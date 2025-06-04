import string
import sys

english = sys.stdin.read()
table = [0] * 26
index = 0
for s in string.ascii_lowercase:
    for t in english:
        if s == t or s.upper() == t:
            table[index] += 1
    index += 1

index = 0
for s in string.ascii_lowercase:
    print("%s : %d" % (s, table[index]))
    index += 1