import sys
a = []
for l in sys.stdin:
    s, w, h = (float(i) for i in l.split(","))
    BMI = w / pow(h, 2)
    if BMI >= 25:
        print(int(s))