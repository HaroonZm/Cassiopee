def main():
    import sys
    input = sys.stdin.readline

    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            break

        era_data = []
        for _ in range(N):
            era_name, era_year_str, western_year_str = input().split()
            era_year = int(era_year_str)
            western_year = int(western_year_str)
            start_year = western_year - (era_year - 1)
            era_data.append((start_year, era_name))
        # Sort eras by their start western year ascending
        era_data.sort(key=lambda x: x[0])

        queries = [int(input()) for _ in range(Q)]

        # For each query, find the era
        for year in queries:
            # Binary search for the closest era with start_year <= year
            left, right = 0, len(era_data)
            while left < right:
                mid = (left + right) // 2
                if era_data[mid][0] <= year:
                    left = mid + 1
                else:
                    right = mid
            era_index = left - 1
            if era_index < 0:
                print("Unknown")
                continue
            # Now check if year falls into era_data[era_index] era or later one
            # If there is a next era starting year and year >= that, unknown
            start_year, era_name = era_data[era_index]
            if era_index + 1 < len(era_data) and year >= era_data[era_index + 1][0]:
                print("Unknown")
            else:
                era_year = year - start_year + 1
                if era_year < 1:
                    print("Unknown")
                else:
                    print(era_name, era_year)


if __name__ == "__main__":
    main()