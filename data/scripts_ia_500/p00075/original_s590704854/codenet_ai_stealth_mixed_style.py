import sys
a = []
def calculate_bmi(w, h):
    return w / (h ** 2)

for line in sys.stdin:
    parts = line.strip().split(",")
    s = float(parts[0])
    w = float(parts[1])
    h = float(parts[2])
    BMI = calculate_bmi(w, h)
    if BMI >= 25:
        print(int(s))