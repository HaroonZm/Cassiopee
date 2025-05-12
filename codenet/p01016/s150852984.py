a = input()
b = input()

for i in range(len(a) - len(b) + 1):
    f = True
    for j in range(len(b)):
        if a[i+j] == b[j]:
            pass
        else:
            if b[j] == '_':
                pass
            else:
                f = False
                break
    if f:
        print('Yes')
        exit()
print('No')