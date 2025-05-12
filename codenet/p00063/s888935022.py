import sys
print sum([1 for line in map(lambda x:x.strip(),sys.stdin.readlines()) if line==line[::-1]])