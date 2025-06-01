era_type, year_value = map(int, input().split())

era_offsets = [0, 1867, 1911, 1925, 1988]

if era_type == 0:

    if year_value > 1988:
        print(f'H{year_value - 1988}')
    
    elif year_value > 1925:
        print(f'S{year_value - 1925}')
    
    elif year_value > 1911:
        print(f'T{year_value - 1911}')
    
    else:
        print(f'M{year_value - 1867}')

else:

    print(era_offsets[era_type] + year_value)