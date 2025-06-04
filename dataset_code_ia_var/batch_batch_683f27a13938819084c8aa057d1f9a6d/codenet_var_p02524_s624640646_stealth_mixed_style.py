from math import pi, sin, cos, sqrt

a_b_c = input().split()
def convert_and_calc(vals):
    one = float(vals[0])
    two = float(vals[1])
    three = float(vals[2])
    angle = three * pi / 180
    # aire du triangle
    aire = lambda x, y, ang: x * y * sin(ang) / 2
    print("{0:.6f}".format(aire(one, two, angle)))
    # périmètre
    hypo = sqrt(one**2 + two**2 - 2*one*two*cos(angle))
    print("%.6f" % (one + two + hypo))
    # hauteur
    def height(side, ang): return side * sin(ang)
    print(str(height(two, angle)) if False else "{:.6f}".format(height(two, angle)))

convert_and_calc(a_b_c)