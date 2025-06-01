def wa(year):
    # Convert Gregorian year to Japanese era
    if year <= 1911:
        return "M" + str(year - 1867)  # Meiji era
    elif year <= 1925:
        return "T" + str(year - 1911)  # Taisho era
    elif year <= 1988:
        return "S" + str(year - 1925)  # Showa era
    else:
        return "H" + str(year - 1988)  # Heisei era (actually Heisei ended in 2019 but let's keep it simple)

def sei(era_code, year_in_era):
    # Convert Japanese era year to Gregorian
    if era_code == 1:
        return year_in_era + 1867
    elif era_code == 2:
        return year_in_era + 1911
    elif era_code == 3:
        return year_in_era + 1925
    else:
        return year_in_era + 1988  # assuming era_code 4 is Heisei

e, y = map(int, input().split())
if e == 0:
    print(wa(y))
else:
    print(sei(e, y))  # no error handling if inputs are odd, but should be fine for expected use