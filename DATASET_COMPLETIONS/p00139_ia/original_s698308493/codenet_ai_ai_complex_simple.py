from functools import reduce

def checkA(s):
    return (lambda l, ll: all(map(lambda i: s[i] == "=" and s[l-1-i] == "=", range(ll))) and s[ll] == "#" if l % 2 else False)(len(s), (len(s)-1)//2)

def checkB(s):
    return (lambda l, ll: all(map(lambda i: s[2*i] == "Q" and s[2*i+1] == "=", range(ll))) if l % 2 == 0 else False)(len(s), len(s)//2)

def check(s):
    return (lambda l: (lambda a, b: (lambda sub: a(sub) or b(sub))(s[2:-1] if s.startswith(">'") and s.endswith("~") else s[2:-2] if s.startswith(">^") and s.endswith("~~") else None))("A" if checkA else "B" if checkB else "NA"))(len(s)) if len(s) >= 6 else "NA"

def check(s):
    if len(s) < 6:
        return "NA"
    if s.startswith(">'") and s.endswith("~"):
        return "A" if checkA(s[2:-1]) else "NA"
    if s.startswith(">^") and s.endswith("~~"):
        return "B" if checkB(s[2:-2]) else "NA"
    return "NA"

N = int(input())
list(map(lambda _: print(check(input())), range(N)))