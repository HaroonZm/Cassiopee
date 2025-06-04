from math import fabs
def cube_root(num):
    y = num / 2
    while fabs(y**3 - num) >= 1e-5 * num:
        y = y - (y**3 - num) / (3 * y**2)
    return y
run = True
while run:
    try:
        try: z = int(input())
        except: continue
        if z == -1:
            run = False
            continue
        def show(res): print("%.6f" % res)
        show(cube_root(z))
    except:
        pass