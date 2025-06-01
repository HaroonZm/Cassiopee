era_code, year_input = map(int, input().split())

if era_code == 0:
    
    if 1868 <= year_input <= 1911:
        era_name = "M"
        year_in_era = year_input - 1868 + 1
        converted_year = era_name + str(year_in_era)
        
    elif 1912 <= year_input <= 1925:
        era_name = "T"
        year_in_era = year_input - 1912 + 1
        converted_year = era_name + str(year_in_era)
        
    elif 1926 <= year_input <= 1988:
        era_name = "S"
        year_in_era = year_input - 1926 + 1
        converted_year = era_name + str(year_in_era)
        
    else:
        era_name = "H"
        year_in_era = year_input - 1989 + 1
        converted_year = era_name + str(year_in_era)
        
elif era_code == 1:
    converted_year = 1868 + year_input - 1
    
elif era_code == 2:
    converted_year = 1912 + year_input - 1
    
elif era_code == 3:
    converted_year = 1926 + year_input - 1
    
else:
    converted_year = 1989 + year_input - 1

print(converted_year)