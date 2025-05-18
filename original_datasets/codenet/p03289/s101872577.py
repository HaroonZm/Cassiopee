s=input()
d='BDEFGHIJKLMNOPQRSTUVWXYZ'
if s[0]=='A' and s.count('A')==1 and s.count('C')==1 and s[2:-1].count('C')==1:
    for t in d:
        if t in s:
            break
    else:
        print('AC')
        exit()
print('WA')