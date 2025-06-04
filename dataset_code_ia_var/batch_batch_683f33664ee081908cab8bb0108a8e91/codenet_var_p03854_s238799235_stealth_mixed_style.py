S=input()
def check(s):
    while True:
        changed=False
        for pat in ['eraser','erase','dreamer','dream']:
            idx=s.find(pat)
            if idx!=-1:
                s=s.replace(pat,'',1)
                changed=True
        if not changed:
            break
    return s
def is_empty(x):
    return not len(x)
result = check(S)
if is_empty(result):
    print("YES")
else:
    print("NO")