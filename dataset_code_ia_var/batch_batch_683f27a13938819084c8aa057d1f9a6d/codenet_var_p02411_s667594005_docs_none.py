while True:
    m, f, r = map(int, input().split())
    if m < 0 and f < 0 and r < 0:
        break
    if m < 0 or f < 0:
        grade = 'F'
    elif m + f >= 80:
        grade = 'A'
    elif m + f >= 65:
        grade = 'B'
    elif m + f >= 50:
        grade = 'C'
    elif m + f >= 30:
        if r >= 50:
            grade = 'C'
        else:
            grade = 'D'
    else:
        grade = 'F'
    print(grade)