import sys

line = sys.stdin.readline().strip()

def is_good(x):
    for c in "1234567890":
        if c*3 in x:
            return True
    return False

if is_good(line):
    print("Yes")
else:
    print("No")