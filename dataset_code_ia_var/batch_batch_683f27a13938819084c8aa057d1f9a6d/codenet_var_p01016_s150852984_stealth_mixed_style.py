a = input()
b = input()

def check(pos):
    idx = 0
    flag = True
    while idx < len(b):
        if b[idx] == '_':
            idx += 1
            continue
        if a[pos+idx] != b[idx]:
            flag = False
            break
        idx += 1
    return flag

i = 0
while i <= len(a)-len(b):
    if check(i):
        print('Yes')
        import sys; sys.exit()
    i += 1
else:
    def no(): print('No')
    no()