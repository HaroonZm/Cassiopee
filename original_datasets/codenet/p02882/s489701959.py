import math

a, b, x = map(int, input().split())

if x/(a*a*b) <= 0.5: #水が水筒の半分以下の場合
    h = x/a/b*2
    hy2 = (h*h + b*b)
    cosa = (hy2 + b*b - h*h )/(2*(hy2**0.5)*b)
    d = 180 - math.degrees(math.acos(cosa)) - 90
else:
    rest = (a*a*b - x)/a
    tan = rest*2/(a*a) #空の部分の面積は、a*atanθ/2 = a*a*b - x
    d = math.degrees(math.atan(tan))

print(d)