n = int(input())
for i in range(n):
    s = input().strip()
    t = input().strip()
    for c in s[::-1]:
        if c == 'J':
            t = t[-1:] + t[:-1]
        elif c == 'C':
            t = t[1:] + t[0]
        elif c == 'E':
            t = t[(len(t)+1)//2:] + t[len(t)//2:(len(t)+1)//2] + t[:len(t)//2]
        elif c == 'A':
            t = t[::-1]
        elif c == 'P':
            t = t.translate(str.maketrans('0123456789', '9012345678'))
        elif c == 'M':
            t = t.translate(str.maketrans('0123456789', '1234567890'))
    print(t)