import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    y, m, d = map(int, line.split())

    # define era start and end dates
    # each as (year, month, day)
    meiji_start = (1868, 9, 8)
    meiji_end = (1912, 7, 29)

    taisho_start = (1912, 7, 30)
    taisho_end = (1926, 12, 24)

    showa_start = (1926, 12, 25)
    showa_end = (1989, 1, 7)

    heisei_start = (1989, 1, 8)

    input_date = (y, m, d)

    def date_less_equal(a, b):
        # return True if date a <= date b
        if a[0] < b[0]:
            return True
        elif a[0] > b[0]:
            return False
        else:
            if a[1] < b[1]:
                return True
            elif a[1] > b[1]:
                return False
            else:
                if a[2] <= b[2]:
                    return True
                else:
                    return False

    def date_greater_equal(a, b):
        # return True if date a >= date b
        if a[0] > b[0]:
            return True
        elif a[0] < b[0]:
            return False
        else:
            if a[1] > b[1]:
                return True
            elif a[1] < b[1]:
                return False
            else:
                if a[2] >= b[2]:
                    return True
                else:
                    return False

    if date_less_equal(input_date, (1868, 9, 7)):
        print("pre-meiji")
    elif date_greater_equal(input_date, meiji_start) and date_less_equal(input_date, meiji_end):
        era = "meiji"
        year = y - 1867
        print(era, year, m, d)
    elif date_greater_equal(input_date, taisho_start) and date_less_equal(input_date, taisho_end):
        era = "taisho"
        year = y - 1911
        print(era, year, m, d)
    elif date_greater_equal(input_date, showa_start) and date_less_equal(input_date, showa_end):
        era = "showa"
        year = y - 1925
        print(era, year, m, d)
    elif date_greater_equal(input_date, heisei_start):
        era = "heisei"
        year = y - 1988
        print(era, year, m, d)
    else:
        # for safety, print pre-meiji if none match.
        print("pre-meiji")