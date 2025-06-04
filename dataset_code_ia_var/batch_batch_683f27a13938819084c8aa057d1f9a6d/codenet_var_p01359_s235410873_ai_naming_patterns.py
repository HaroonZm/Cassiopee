import sys
from bisect import bisect_left

def main():
    while True:
        num_eras, num_queries = map(int, input().split())
        if num_eras == 0:
            break

        era_dict = {}
        era_start_years = []

        for _ in range(num_eras):
            era_name, era_local_year, era_start_year = input().split()
            era_local_year = int(era_local_year)
            era_start_year = int(era_start_year)
            era_dict[era_start_year] = (era_name, era_local_year)
            era_start_years.append(era_start_year)

        era_start_years_sorted = sorted(era_start_years)

        for _ in range(num_queries):
            query_year = int(input())
            idx = bisect_left(era_start_years_sorted, query_year)

            if idx >= len(era_start_years_sorted):
                print('Unknown')
                continue

            selected_start_year = era_start_years_sorted[idx]
            selected_era_name, selected_era_local_year = era_dict[selected_start_year]
            local_year = query_year - selected_start_year + selected_era_local_year

            if local_year <= 0:
                print('Unknown')
            else:
                print(selected_era_name, local_year)

main()