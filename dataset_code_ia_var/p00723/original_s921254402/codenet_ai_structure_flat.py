m = int(input())
for _ in range(m):
    d = input()
    _set = set()
    for i in range(len(d)-1):
        w1 = d[:i+1]
        w2 = d[i+1:]
        rw1 = ''.join(list(reversed(w1)))
        rw2 = ''.join(list(reversed(w2)))
        _set.add(w1 + w2)
        _set.add(w2 + w1)
        _set.add(rw1 + rw2)
        _set.add(rw2 + rw1)
        _set.add(w1 + rw2)
        _set.add(w2 + rw1)
        _set.add(rw1 + w2)
        _set.add(rw2 + w1)
    print(len(_set))