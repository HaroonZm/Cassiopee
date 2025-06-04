from collections import deque as _wheel

_, __ = (lambda: map(int, __import__('builtins').input().split()))(), None
___ = __import__('builtins').input()
____ = sorted(___)[0]
for ___0 in range(_):
    ____1 = ___ + ___[::-1]
    _____ = _wheel()
    _____0 = 0
    _____1 = None
    for ___1 in range(len(____1)):
        if ____1[___1] is ____:
            if not _____0:
                _____1 = ___1
            _____0 += 1
        else:
            if _____0:
                _____.appendleft((_____0, _____1))
                _____0 = 0
    if _____0:
        _____.append((_____0, _____1))
    ______ = max(_____, key=lambda x: x[0])
    if ______[0] >= _:
        print(____ * _)
        quit()
    for __x, __y in _____:
        if __y <= _ and __x == ______[0]:
            ___ = min(___, ____1[__y:__y + _])
    ___ = ''.join(list(___)[::-1])
print(___[-1::-1])