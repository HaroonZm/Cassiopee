import sys
f = sys.stdin

def somme():
    return sum(int(i) for i in f.readline().split())

s = somme()
t = somme()

print(t if t > s else s)