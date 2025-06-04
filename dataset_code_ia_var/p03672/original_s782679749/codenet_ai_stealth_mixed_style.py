from functools import reduce

def get_input():
    return input()

def update_m(m, cond, val):
    if cond: return val
    return m

s = get_input()
m = 0

if s[0] == s[1]:
    m = 1

def check_prefix(i):
    if i == len(s)//2 - 1:
        return None
    if s[:i] == s[i:2*i]:
        return i
    return None

i = 1
while i < (len(s)//2):
    result = check_prefix(i)
    if result is not None:
        m = result
    if i == len(s)//2-1:
        break
    i += 1

print(2*m)