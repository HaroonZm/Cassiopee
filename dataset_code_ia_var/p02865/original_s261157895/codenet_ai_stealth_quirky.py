N=int(input())
a=None
try:
    _even = not N%2
    a = (N//2)-int(_even)
finally:
    [print(a) for _ in range(1)]