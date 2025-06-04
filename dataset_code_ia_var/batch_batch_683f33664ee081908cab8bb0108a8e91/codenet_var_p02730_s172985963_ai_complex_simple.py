from functools import reduce
from operator import mul

s = input()
n = len(s)

palindrome = lambda x: reduce(lambda a,b: a and b, map(lambda i: x[i]==x[~i], range(len(x)//2)), True)
halves = [(slice(0, n//2), slice(0, n//2)), (slice((n+2)//2, None), slice((n+2)//2, None))]

if palindrome(s) and all(palindrome(s[slc]) for slc,_ in halves):
    print("Yes")
    raise SystemExit
print("No")