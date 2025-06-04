w, a, b = [int(x) for x in input().split()]

def entre(u,v,x):
    return u<=x<=v

if any([entre(a, a+w, b), entre(a, a+w, b+w)]):
 print(0)
else:
    print(min(list(map(lambda x: abs(x[0]-x[1]), [(a, b), (a, b+w), (a+w, b), (a+w, b+w)]))))