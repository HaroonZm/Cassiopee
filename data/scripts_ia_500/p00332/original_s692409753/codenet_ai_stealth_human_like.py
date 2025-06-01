era, year = map(int, input().split())

# Era 0 means convert from Gregorian to Japanese era year
if era == 0:
    if year < 1912:
        print("M" + str(year - 1867))  # Meiji era
    elif year < 1926:
        print("T" + str(year - 1911))  # Taisho era
    elif year < 1989:
        print("S" + str(year - 1925))  # Showa era
    else:
        print("H" + str(year - 1988))  # Heisei era, assuming no Reiwa here
# For era 1 to 4, convert Japanese era year to Gregorian
elif era == 1:
    print(year + 1867)
elif era == 2:
    print(year + 1911)
elif era == 3:
    print(year + 1925)
elif era == 4:
    print(year + 1988)
# no else, assuming input is valid