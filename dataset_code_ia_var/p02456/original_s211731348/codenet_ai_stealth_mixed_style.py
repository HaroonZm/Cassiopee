from sys import stdin

q = int(stdin.readline())
S = set()

def process(query, x):
    if query==0:
        S.add(x)
        print(len(S))
    elif query==1:
        print(int(x in S))
    else:
        try:
            S.remove(x)
        except KeyError:
            pass

j = 0
while j < q:
    parts = stdin.readline().split()
    qry = int(parts[0])
    xx = int(parts[1])
    if qry == 0:
        S |= {xx}
        print(len(S))
    elif qry == 1:
        print(1 if xx in S else 0)
    else:
        S.discard(xx)
    j+=1