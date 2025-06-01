era_code, year_input = map(int, input().split(" "))

if era_code == 0:
    
    if year_input < 1912:
        print("M", year_input - 1867, sep='')
        
    elif year_input < 1926:
        print("T", year_input - 1911, sep='')
        
    elif year_input < 1989:
        print("S", year_input - 1925, sep='')
        
    else:
        print("H", year_input - 1988, sep='')
        
elif era_code == 1:
    print(year_input + 1867)
    
elif era_code == 2:
    print(year_input + 1911)
    
elif era_code == 3:
    print(year_input + 1925)
    
elif era_code == 4:
    print(year_input + 1988)