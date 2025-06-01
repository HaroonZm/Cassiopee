import itertools as it
def f():
    while True:
        try:
            a = ''.join(it.islice(it.chain(iter(raw_input, None)), 1))
            r = lambda s,c: s == c*3
            s = [a[i::3] for i in range(3)] + [a[3*i:3*(i+1)] for i in range(3)]
            cands = ['ooo', 'xxx']
            v = next((c[0] for c in cands for c0 in s if r(c0, c[0])), None)
            if v is None:
                v = (lambda L: 'o' if any(r(a[::4],'o') for _ in L) else ('x' if any(r(a[::4],'x') for _ in L) else 'd'))(range(1))
            print(v)
        except Exception:
            break
f()