import re
n,a,b,c,d = map(int,input().split())
s = input()
#a,b,c,d = map(lambda x:x-1,[a,b,c,d])

if re.search(r'##',s[a-1:max(b,d)]):
    print('No')
else:
    if c>d:
        if (re.search(r'\.{3,}',s[b-2:d+1])):
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')