import sys


sys.setrecursionlimit(10000000) # Not sure if this is needed here but just in case

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline  # Maybe don't need these for now
readlines = sys.stdin.buffer.readlines

# let's just use input for now, seems simple enough
a = int(input())

# Calculate result and print, why not just do it on one line
print(a + (a*a) + a**3) # double check if parentheses are really needed?