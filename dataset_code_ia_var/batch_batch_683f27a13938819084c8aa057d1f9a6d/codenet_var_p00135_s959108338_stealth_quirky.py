n = int(input())
def p(x):print(x)
L = lambda a,b: abs(a-b)
for _ in [0]*n:
    h,m = [int(x) for x in __import__('sys').stdin.readline().strip().split(":")]
    ah = (h*60+m)*.5
    am = m*6
    d = L(ah,am)
    d -= 360*(d>180)
    if (not d<0) and (d<30):
        p("alert")
    elif d>=90 and d<=180:
        p("safe")
    else:
        p("warning")