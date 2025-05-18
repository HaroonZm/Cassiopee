import re

A = input()
B = input()

B = B.replace('_', '.')

if re.search(B, A):
    print('Yes')
else:
    print('No')