S = input()
year = int(S[0:4])
month = int(S[5:7])
day = int(S[8:10])
isBefore = False
if year < 2019:
    isBefore = True
if year == 2019:
    if month < 4:
        isBefore = True
    if month == 4:
        if day <= 30:
            isBefore = True
if isBefore:
    print("Heisei")
else:
    print("TBD")