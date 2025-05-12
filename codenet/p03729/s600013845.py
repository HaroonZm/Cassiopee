from sys import stdin

a,b,c = [x for x in stdin.readline().rstrip().split()]

if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")