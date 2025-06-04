triangles = 0
right = 0
acute = 0
obtuse = 0
while True:
    try:
        a,b,c = map(int,input().split())
    except:
        break
    x,y,z = sorted([a,b,c])
    if x + y <= z:
        print(triangles,right,acute,obtuse)
        break
    triangles += 1
    s = x*x + y*y
    z2 = z*z
    if z2 == s:
        right += 1
    elif z2 < s:
        acute += 1
    else:
        obtuse += 1