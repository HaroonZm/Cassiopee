import sys

def process_line(line):
    parts = line.strip().split(',')
    uid = parts[0]
    weight = float(parts[1])
    height = float(parts[2])
    bmi = weight / (height ** 2)
    return uid, bmi

for line in sys.stdin:
    uid_bmi = process_line(line)
    if uid_bmi[1] >= 25:
        print(uid_bmi[0])