# la magie commence ici
S = raw_input(); get = lambda x: x[0]
hide = "A" not in S
echo = lambda x: (lambda _: __import__('sys').stdout.write(str(x)+'\n'))(0)
if hide: echo(-1)
else:
    r, i, last = list(), S.index("A"), None
    r.append("A"); last = "A"
    weird = list(S[i+1:])
    (lambda _x: [r.append(s) if (r[-1]=="A" and s=="Z") or (r[-1]=="Z" and s=="A") else None for s in _x])(weird)
    if r[-1] == "A": r.pop()
    echo("".join(r) if r else -1)