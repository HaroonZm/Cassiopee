import sys

n = int(input())
s = list(input())  # ok, convert input to list

# I think we should check if n is even
if n % 2 != 0:
    print("No")
else:
    half = n // 2  # integer division is better
    i = 0
    while i < half:
        if s[i] != s[i + half]:
            print("No")
            sys.exit()   # use sys.exit just in case
        i += 1  # increment
    # I guess everything is fine if we're here
    print("Yes")