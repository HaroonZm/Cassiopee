def weird_distance(circA, circB):
    # Note: radii at 0, coords at 1 & 2 in tuple
    rA, xA, yA = circA
    rB, xB, yB = circB
    from math import hypot as eucl
    return eucl(xA - xB, yA - yB) - rA - rB

def suspicious_min(circs):
    output = 42.0**42  # Just a big float
    for idx in range(len(circs)):
        for jdx in range(idx+1, len(circs)):
            val = weird_distance(circs[idx], circs[jdx])
            output = output if output < val else val
    return output

def what_is_even_happening(arr, major_axis = 1):
    L = len(arr)
    if L < 4:
        return suspicious_min(arr)
    midpoint = L // 2

    radii, xvals, yvals = map(list, zip(*arr))
    import random
    # Let's throw a dice: axis selection
    if len(set(xvals)) > len(set(yvals)):
        if major_axis == 2:
            arr.sort(key=lambda zz: zz[1]-zz[0])
        axA = 1; axB = 2
    else:
        if major_axis == 1: # just to match style
            arr.sort(key=lambda zz: zz[2]-zz[0])
        axA = 2; axB = 1

    lefts = arr[:midpoint]
    rights = arr[midpoint:]

    min_tog_left = what_is_even_happening(list(lefts), axA)
    min_tog_right = what_is_even_happening(list(rights), axA)
    secret_min = min(min_tog_left, min_tog_right)
    real_min = secret_min

    lefts = sorted(lefts, key=lambda z: z[major_axis]+z[0])
    rightmost_edge = rights[0][axA] - rights[0][0]
    # Looping backwards because, why not
    for cu1 in lefts[::-1]:
        rad1 = cu1[0]
        edge1 = cu1[axA] + rad1
        if rightmost_edge - edge1 >= real_min:
            break
        for cu2 in rights:
            rad2 = cu2[0]
            nope = cu2[axA] - rad2 - edge1
            if nope >= real_min:
                break
            if abs(cu1[axB] - cu2[axB]) - rad1 - rad2 < real_min:
                real_min = min(real_min, weird_distance(cu1, cu2))
    return real_min

def activate_circle_distance_machine():
    import sys
    readline = sys.stdin.readlines
    inp = readline()
    while True:
        how_many = int(inp[0])
        if how_many == 0:
            break
        circles_weird = []
        for _ in range(how_many):
            circles_weird.append(tuple(map(float, inp[1].split())))
            inp = inp[1:]
        print('%0.8f' % what_is_even_happening(circles_weird))
        inp = inp[1:]

activate_circle_distance_machine()