def reverse(s):
    return ''.join(list(reversed(s)))

m = int(input())

for i in range(m):
    d = input()
    _set = set()
    for i in range(len(d)-1):
        w1 = d[:i+1]
        w2 = d[i+1:]
        _set.add(w1 + w2)
        _set.add(w2 + w1)
        _set.add(reverse(w1) + reverse(w2))
        _set.add(reverse(w2) + reverse(w1))
        _set.add(w1 + reverse(w2))
        _set.add(w2 + reverse(w1))
        _set.add(reverse(w1) + w2)
        _set.add(reverse(w2) + w1)

    print(len(_set))