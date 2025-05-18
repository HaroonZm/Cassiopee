import sys
S = raw_input()
d = ["L","R","U","D"]
k = ["R","U","D"]
g = ["L","U","D"]
def r():
    print("No")
    sys.exit()
x = 1
if not (1 <= len(S) and len(S) <= 100): r()
for c in S:
    if not c in d:
        r()
    if(x % 2 == 0):
        if not c in g:
            r()
    else:
        if not c in k:
            r()
    x += 1

print("Yes")