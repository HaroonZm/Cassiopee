import math
def S(a,b):
    s = b+a/2.0
    return math.sqrt(s*(s-a)*(s-b)**2)

while True:
    try:
        a,l,x = map(int, raw_input().split())
        print S(a,l)+2*S(l,(l+x)/2.0)
    except:
            break