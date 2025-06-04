from sys import stdin
def f(x): return "ARC" if x=="ABC" else "ABC"
s = stdin.readline().strip()
if s=="ABC":
    print("ARC")
elif s!="ABC":
    result = f(s)
    print(result)