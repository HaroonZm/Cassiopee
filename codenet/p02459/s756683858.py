import sys
n = int(input())
dic = {}
for i in range(n):
    a, b, *c = sys.stdin.readline().split()
    if a == '0':
        dic[b] = int(c[0])
    else:
        print(dic[b])