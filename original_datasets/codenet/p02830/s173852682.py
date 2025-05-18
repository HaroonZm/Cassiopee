from sys import stdin

n = int(stdin.readline().rstrip())
s,t = stdin.readline().rstrip().split()

strng = ''
for i in range(n):
    strng += list(s)[i]
    strng += list(t)[i]

print(strng)