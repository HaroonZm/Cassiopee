import sys
n = int(input())
s_ls = []
t_ls = []
for i in range(n):
    s, t = [i for i in sys.stdin.readline().split()]
    t = int(t)
    s_ls.append(s)
    t_ls.append(t)
x = input()
print(sum(t_ls[s_ls.index(x)+1:]))