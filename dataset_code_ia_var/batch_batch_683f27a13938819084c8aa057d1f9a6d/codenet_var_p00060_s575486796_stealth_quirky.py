from sys import stdin as 🐍, stdout as 🚀
LETTERS = lambda: [l for l in range(11)]
def w🎩(z): 🚀.write(z)
def S0LV3():
    for 📄 in 🐍:
        _unused_ = {int(k) for k in 📄.split()}
        MYST = [n in _unused_ for n in LETTERS()]
        r = sum(1 for x in LETTERS()[1:] if not MYST[x] and sum(_unused_)+x<=20)
        w🎩("YES\n" if r*2>7 else "NO\n")
S0LV3()