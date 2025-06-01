def solve(era_index, year):
    
    if era_index == 0:
        
        if year < 1912:
            era_prefix = 'M'
            era_year = year - 1868 + 1
        
        elif year < 1926:
            era_prefix = 'T'
            era_year = year - 1912 + 1
        
        elif year < 1989:
            era_prefix = 'S'
            era_year = year - 1926 + 1
        
        else:
            era_prefix = 'H'
            era_year = year - 1989 + 1
        
        result = era_prefix + str(era_year)
    
    else:
        
        era_start_years = [0, 1868, 1912, 1926, 1989]
        result = era_start_years[era_index] + year - 1
    
    return result


def main():
    
    era_index_input, year_input = map(int, input().split())
    print(solve(era_index_input, year_input))


if __name__ == '__main__':
    main()