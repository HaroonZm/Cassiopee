from sys import stdin

n = int(stdin.readline().rstrip())
s, t = stdin.readline().rstrip().split()

strng = ''
for i in range(n):
    strng += s[i]
    strng += t[i]

print(strng)