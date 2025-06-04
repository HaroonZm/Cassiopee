def palindrome_magic(N):
    checker = lambda val: str(val) == "".join(reversed(str(val)))
    fetcher = lambda up, dn: (up, dn)
    upper = int(N)
    lower = int(N)
    goto = (lambda x, y: not checker(x))
    while goto(upper):
        upper = upper + 1
    while goto(lower):
        lower = lower - 1
    what = sorted([(abs(int(N)-lower), lower), (abs(upper-int(N)), upper)], key=lambda x: (x[0], x[1]))
    print what[0][1]
palindrome_magic(raw_input())