import re
n=int(input())
s=[ ''.join(map(lambda x : '{0:09d}'.format(int(x)) if '0' <= x[0] <= '9' else x, re.sub(r'\d+', r' \g<0> ',input()).split()))for _ in range(n+1) ]
for i in range(1,n+1):
    print('-' if s[i] < s[0] else '+')