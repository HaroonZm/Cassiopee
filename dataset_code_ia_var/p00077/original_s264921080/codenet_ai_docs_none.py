import re,sys

for s in sys.stdin:
    l = re.split('(@.{2})', s)
    for s in l:
        if '@' in s:
            s = s[2] * int(s[1])
        sys.stdout.write(s)