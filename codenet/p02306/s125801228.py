import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

#3辺の長さ
a = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
b = math.sqrt(((x3-x2)**2)+((y3-y2)**2))
c = math.sqrt(((x1-x3)**2)+((y1-y3)**2))
s = (a+b+c)/2

r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s #ヘロンの公式
xa, ya = x1+(x2-x1)*c/(b+c), y1+(y2-y1)*c/(b+c) #二等分線とaの交点
xb, yb = x2+(x3-x2)*a/(a+c), y2+(y3-y2)*a/(a+c)

if (xa-x3) != 0 and (xb-x1) != 0:
    a1, b1 = (ya-y3)/(xa-x3), -((ya-y3)/(xa-x3))*x3+y3 #二等分線の方程式
    a2, b2 = (yb-y1)/(xb-x1), -((yb-y1)/(xb-x1))*x1+y1
    cx = (b2-b1)/(a1-a2)
    cy = a1 * cx + b1

if xa-x3 == 0:
    cx = x3
    a2, b2 = (yb-y1)/(xb-x1), -((yb-y1)/(xb-x1))*x1+y1
    cy = a2 * cx + b2

if xb-x1 == 0:
    cx = x1
    a1, b1 = (ya-y3)/(xa-x3), -((ya-y3)/(xa-x3))*x3+y3
    cy = a1 * cx + b1

print(cx, cy, r)