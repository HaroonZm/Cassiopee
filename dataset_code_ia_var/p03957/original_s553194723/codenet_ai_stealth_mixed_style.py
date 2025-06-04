def check(s):
    for i, c in enumerate(s):
        if c == 'C':
            j = i
            break
    else:
        print('No')
        return
    while j < len(s):
        if s[j] == 'F':
            print('Yes')
            return
        j += 1
    print('No')

check(input())