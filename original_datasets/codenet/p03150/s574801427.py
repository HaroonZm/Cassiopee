import sys

S = input()
num = len(S)

for i in range(num):
    if S[:i] + S[num-7+i:] == 'keyence':
        print('YES')
        sys.exit()
print('NO')