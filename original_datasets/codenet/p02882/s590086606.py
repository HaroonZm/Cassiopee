import math

a, b, x = map(int, input().split())

vol = a**2 * b
ans = 0
if vol/2 < x:
    #print("水多し、台形になる")
    h0 = x/(a**2)
    c = 2*h0 - b
    ans = math.degrees(math.atan((b-c)/a))
else:
    #print("水少ない、三角形になる")
    d = (2*x)/(b*a)
    ans = math.degrees(math.atan(b/d))
print(ans)