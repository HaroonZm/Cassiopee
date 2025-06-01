import datetime
while True:
    inputs = input()
    values = inputs.split()
    y1 = int(values[0])
    if y1 < 0:
        break
    m1 = int(values[1])
    d1 = int(values[2])
    y2 = int(values[3])
    m2 = int(values[4])
    d2 = int(values[5])
    start_date = datetime.date(y1, m1, d1)
    end_date = datetime.date(y2, m2, d2)
    difference = end_date - start_date
    print(difference.days)