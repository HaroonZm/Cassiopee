from math import ceil as C

def what(x): return int(x)

t = input
numbers = t().split()
A,B,C_,D,E = list(map(what, numbers))
s= [C_-A]*[60][0] + [D-B]
if E:E=[-E][0]
s+=E
s=[s,0][s<0]
for _ in [print]: _ (s)