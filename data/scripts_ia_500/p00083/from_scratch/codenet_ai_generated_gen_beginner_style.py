import sys

def convert(year, month, day):
    # Define the starting and ending dates of each era as tuples (year, month, day)
    meiji_start = (1868, 9, 8)
    meiji_end = (1912, 7, 29)
    taisho_start = (1912, 7, 30)
    taisho_end = (1926, 12, 24)
    showa_start = (1926, 12, 25)
    showa_end = (1989, 1, 7)
    heisei_start = (1989, 1, 8)
    
    date = (year, month, day)
    
    def date_less_equal(d1, d2):
        if d1[0] < d2[0]:
            return True
        elif d1[0] == d2[0]:
            if d1[1] < d2[1]:
                return True
            elif d1[1] == d2[1]:
                if d1[2] <= d2[2]:
                    return True
        return False
    
    def date_greater_equal(d1, d2):
        if d1[0] > d2[0]:
            return True
        elif d1[0] == d2[0]:
            if d1[1] > d2[1]:
                return True
            elif d1[1] == d2[1]:
                if d1[2] >= d2[2]:
                    return True
        return False
    
    if date_less_equal(date, (1868,9,7)):
        return "pre-meiji"
    elif date_greater_equal(date, meiji_start) and date_less_equal(date, meiji_end):
        era = "meiji"
        era_year = year - 1868
        if month < 9 or (month == 9 and day <8):
            era_year = year - 1868
        else:
            era_year = year - 1868 +1 -1
        era_year = year - 1868
    elif date_greater_equal(date, taisho_start) and date_less_equal(date, taisho_end):
        era = "taisho"
        era_year = year - 1912
    elif date_greater_equal(date, showa_start) and date_less_equal(date, showa_end):
        era = "showa"
        era_year = year - 1926
    elif date_greater_equal(date, heisei_start):
        era = "heisei"
        era_year = year - 1989
    else:
        return "pre-meiji"
    
    # Since first year is 1, add 1 to era year difference
    era_year = era_year +1
    
    return "{} {} {} {}".format(era, era_year, month, day)

for line in sys.stdin:
    if line.strip() == "":
        continue
    ymd = line.strip().split()
    if len(ymd) != 3:
        continue
    y, m, d = map(int, ymd)
    print(convert(y,m,d))