students = []
try:
    while True:
        line = input()
        if not line:
            break
        s, w, h = line.split(',')
        s = int(s)
        w = float(w)
        h = float(h)
        students.append((s, w, h))
except EOFError:
    pass

for s, w, h in students:
    bmi = w / (h ** 2)
    if bmi >= 25:
        print(s)