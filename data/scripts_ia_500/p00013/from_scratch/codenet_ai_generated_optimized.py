stack = []
import sys
for line in sys.stdin:
    x = line.strip()
    if not x:
        continue
    x = int(x)
    if x == 0:
        print(stack.pop())
    else:
        stack.append(x)