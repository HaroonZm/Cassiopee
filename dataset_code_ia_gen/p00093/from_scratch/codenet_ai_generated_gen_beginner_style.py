def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

while True:
    line = input()
    if line == "":
        continue
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    leap_years = []
    for year in range(a, b + 1):
        if is_leap_year(year):
            leap_years.append(year)
    if len(leap_years) == 0:
        print("NA")
    else:
        for y in leap_years:
            print(y)
    print()