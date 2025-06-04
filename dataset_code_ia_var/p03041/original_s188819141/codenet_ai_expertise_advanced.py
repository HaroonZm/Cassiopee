from sys import stdout

n, k = map(int, input().split())
s = list(input())
s[k - 1] = s[k - 1].lower()
stdout.write(''.join(s))