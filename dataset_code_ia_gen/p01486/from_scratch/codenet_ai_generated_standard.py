import sys
sys.setrecursionlimit(10**7)

S = input()

def parse(s, i):
    if i == len(s):
        return True, i  # empty string is valid
    if i >= len(s) or s[i] != 'm':
        return False, i
    i += 1
    ok1, i = parse(s, i)
    if not ok1:
        return False, i
    if i >= len(s) or s[i] != 'e':
        return False, i
    i += 1
    ok2, i = parse(s, i)
    if not ok2:
        return False, i
    if i >= len(s) or s[i] != 'w':
        return False, i
    i += 1
    return True, i

ok, pos = parse(S, 0)
print("Cat" if ok and pos == len(S) else "Rabbit")