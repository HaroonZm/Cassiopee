#encoding=utf-8

import sys
count = 0
for line in sys.stdin:
    word = line[:-1]
    if word == word[::-1]: count += 1
print count