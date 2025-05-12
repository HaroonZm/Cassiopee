while 1:
    s=input()
    if s=='#':
        break
    s=s.split('/')
    field=[list(''.join(['b' if c=='b' else '.'*int(c) for c in s[i]]))  for i in range(len(s))]
    a,b,c,d=map(int,input().split())
    field[a-1][b-1],field[c-1][d-1]='.','b'
    print('/'.join(['b'.join('' if len(c)==0 else str(len(c)) for c in ''.join(field[i]).split('b') ) for i in range(len(field))]))