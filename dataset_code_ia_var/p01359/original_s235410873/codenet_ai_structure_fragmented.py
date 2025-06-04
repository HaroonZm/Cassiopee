from bisect import bisect_left

def read_n_q():
    return map(int, input().split())

def is_end(n):
    return n == 0

def read_era_entry():
    gengou, wa_year, we_year = input().split()
    return gengou, int(wa_year), int(we_year)

def process_era_entry(era, years, gengou, wa_year, we_year):
    era[we_year] = (gengou, wa_year)
    years.append(we_year)

def sort_years(years):
    return sorted(years)

def read_query_year():
    return int(input())

def get_era_index(years_final, year1):
    return bisect_left(years_final, year1)

def is_unknown_index(index, years_final):
    return index >= len(years_final)

def get_era_info(era, years_final, index):
    year2 = years_final[index]
    gengou, span = era[year2]
    return gengou, span, year2

def calc_result(year1, year2, span):
    return year1 - year2 + span

def is_unknown_result(result):
    return result <= 0

def handle_unknown():
    print('Unknown')

def handle_known(gengou, result):
    print(gengou, result)

def handle_query(era, years_final):
    year1 = read_query_year()
    temp = get_era_index(years_final, year1)
    if is_unknown_index(temp, years_final):
        handle_unknown()
        return
    gengou, span, year2 = get_era_info(era, years_final, temp)
    result = calc_result(year1, year2, span)
    if is_unknown_result(result):
        handle_unknown()
    else:
        handle_known(gengou, result)

def handle_test_case(n, q):
    era = {}
    years = []
    for _ in range(n):
        gengou, wa_year, we_year = read_era_entry()
        process_era_entry(era, years, gengou, wa_year, we_year)
    years_final = sort_years(years)
    for _ in range(q):
        handle_query(era, years_final)

def main():
    while True:
        n, q = read_n_q()
        if is_end(n):
            break
        handle_test_case(n, q)

main()