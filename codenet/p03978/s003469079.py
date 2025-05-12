from sys import stdout
n = int(raw_input())
def req(b):
    print b[0]
    print b[1]
    stdout.flush()
    return raw_input().strip()
s = ['..', '.#', '#.', '##']
a = ['', '']
while 1:
    for t in s:
        b = [a[0] + t[0], a[1] + t[1]]
        r = req(b)
        if r == 'end':
            quit()
        if r == 'T':
            a = b
            break
    else:
        break
while 1:
    for t in s:
        b = [t[0] + a[0], t[1] + a[1]]
        r = req(b)
        if r == 'end':
            quit()
        if r == 'T':
            a = b
            break
    else:
        break