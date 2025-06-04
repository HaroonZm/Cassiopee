import sys

for line in sys.stdin:
    s = line.strip()
    result = ''
    i = 0
    while i < len(s):
        if s[i] == '@':
            count = int(s[i+1])
            char = s[i+2]
            result += char * count
            i += 3
        else:
            result += s[i]
            i += 1
    print(result)