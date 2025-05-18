import sys
print("\n".join(map(str, [int(s) for l in sys.stdin for s, w, h in [map(float, l.split(","))] if w/h**2 >= 25])))