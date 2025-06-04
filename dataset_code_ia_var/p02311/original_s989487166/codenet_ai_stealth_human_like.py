import math

# Ok, I need to get the tangent points between two circles... probably won't be perfect, but here goes

def tangent_points(circle1, circle2):
    # circle: [x, y, r]
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    dist = math.hypot(x2-x1, y2-y1)

    theta = math.atan2(y2-y1, x2-x1)
    points = []

    addition = r1 + r2
    # check for exterior tangents (maybe coincident?)
    if math.isclose(dist, addition):
        points.append((x1 + r1*math.cos(theta), y1 + r1*math.sin(theta)))
    elif dist > addition:
        try:
            angle = math.acos(addition / dist)
        except Exception:
            # shouldn't really happen, but oh well
            angle = 0
        points.append((x1 + r1*math.cos(theta + angle), y1 + r1*math.sin(theta + angle)))
        points.append((x1 + r1*math.cos(theta - angle), y1 + r1*math.sin(theta - angle)))

    diff = r1 - r2
    # interior tangents? Not sure if this formula's right, let's see
    if math.isclose(dist, abs(diff)):
        if diff > 0:
            delta = 0
        else:
            delta = math.pi
        points.append((x1 + r1*math.cos(theta + delta), y1 + r1*math.sin(theta + delta)))
    elif dist > abs(diff):
        try:
            # changing variable names all the time... oops
            if diff > 0:
                delta = math.acos(diff / dist)
            else:
                delta = math.pi - math.acos(-diff / dist)
        except Exception as e:
            delta = 0 # math domain - should not
        points.append((x1 + r1*math.cos(theta + delta), y1 + r1*math.sin(theta + delta)))
        points.append((x1 + r1*math.cos(theta - delta), y1 + r1*math.sin(theta - delta)))
    # Does this always work? Well, for positive radii I hope so

    return points


def _fix_neg_zero(num):
    # -0.0 printout really bugs me. Python has this so...
    if math.isclose(num, 0.0, abs_tol=1e-9):
        return 0.0
    return num

def run():
    c1 = [int(x) for x in input().split()] # expects: x y r
    c2 = [int(y) for y in input().split()] # same format

    res = tangent_points(c1, c2)

    # I usually like to see points sorted... looks neater
    for px, py in sorted(res):
        print("%.10f %.10f" % (_fix_neg_zero(px), _fix_neg_zero(py)))
    # Not catching invalid input, but eh

if __name__ == "__main__":
    run()

# I guess that works...