from itertools import islice

def is_embedded(s, t):
    it = iter(t)
    return all(any(c == x or next(it, None) for x in it) for c in s)

s = input()
t = input()
result = any(
    lambda sub_s: all((c := next((x for x in iter(t)), None)) == ch for ch in sub_s)
    for sub_s in (s, s[1:])
)

# Using more advanced constructs
def check(s, t):
    it = iter(t)
    return all(any(c == ch or next(it, None) for c in it) for ch in s)

print('Yes' if check(s, t) or check(s[1:], t) else 'No')