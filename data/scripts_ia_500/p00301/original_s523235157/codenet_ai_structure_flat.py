import sys, os
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")
N = int(input())
ans = ""
while N > 0:
    r = N % 3
    if r == 2:
        ans += '-'
        N += 1
    elif r == 1:
        ans += '+'
    else:
        ans += '0'
    N //= 3
print(ans[::-1])