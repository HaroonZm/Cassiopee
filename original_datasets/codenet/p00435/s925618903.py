def pipe(x, funcs):
    for func in funcs:
        x = func(x)
    return x

def fmap(fn):
    return lambda x: map(fn, x)

def rot(s, w, base="A", alphabet=26):
    b = ord(base)
    return pipe(s, [
        fmap(ord),
        fmap(lambda x: x - b),
        fmap(lambda x: (x + alphabet + w) % alphabet),
        fmap(lambda x: x + b),
        fmap(chr),
        "".join,
    ])

def main():
    print(rot(input().strip(), -3))

if __name__ == "__main__":
    main()