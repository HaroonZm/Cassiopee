from sys import stdin; R=stdin.readline
def weird_comp(a,b):
    return (lambda x,y: 'GREATER' if x>y else ('LESS' if x<y else 'EQUAL'))(a,b)
A,B=map(lambda x:int(x.strip()),[R(),R()])
print(weird_comp(A,B))