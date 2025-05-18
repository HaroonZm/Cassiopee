sx,sy,tx,ty=map(int,input().split())
d=tx-sx
h=ty-sy
s='U'*h+'R'*d+'D'*h+'L'*(1+d)+'U'*(1+h)+'R'*(1+d)+'D'+'R'+'D'*(h+1)+'L'*(d+1)+'U'
print(s)