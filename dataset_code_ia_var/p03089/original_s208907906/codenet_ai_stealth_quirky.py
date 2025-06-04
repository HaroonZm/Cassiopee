x = lambda: int(__import__('builtins').input())
y = lambda: list(map(int, __import__('builtins').input().split()))
A = x()
_ = y()
B = []
is_over = 0

loop = True
while loop:
    found = 'no'
    idx = len(_) - 1
    while idx >= 0:
        if _[idx] == idx + 1:
            found = 'yes'
            B += [_[idx]]
            _ = _[:idx] + _[idx+1:]
            break
        idx -= 1
    if found == 'no':
        [print(-1), exit()]
    if not _:
        loop = False

[print(B[j]) for j in range(len(B)-1, -1, -1)]