students = []
while True:
    try:
        line = input()
        if line == "":
            break
        parts = line.split(",")
        s = int(parts[0])
        w = float(parts[1])
        h = float(parts[2])
        students.append((s, w, h))
    except:
        break

for s, w, h in students:
    bmi = w / (h * h)
    if bmi >= 25:
        print(s)