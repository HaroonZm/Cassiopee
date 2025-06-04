from sys import stdin

S = stdin.readline().rstrip()
print('2018', *S.split()[0][4:], sep='')