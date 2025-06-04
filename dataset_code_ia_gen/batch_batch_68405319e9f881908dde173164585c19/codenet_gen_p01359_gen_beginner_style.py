while True:
    line = input()
    if line == '0 0':
        break
    N, Q = map(int, line.split())
    era_data = []
    for _ in range(N):
        era_name, era_year_s, western_year_s = input().split()
        era_year = int(era_year_s)
        western_year = int(western_year_s)
        start_year = western_year - era_year + 1
        era_data.append((start_year, era_name))
    era_data.sort(key=lambda x: x[0])
    query_years = []
    for _ in range(Q):
        query_years.append(int(input()))
    for y in query_years:
        # find which era the year belongs to
        era_found = False
        for i in range(len(era_data)):
            start, name = era_data[i]
            if y < start:
                continue
            # check next era start if exists
            if i == len(era_data) -1 or y < era_data[i+1][0]:
                era_year = y - start + 1
                print(name, era_year)
                era_found = True
                break
        if not era_found:
            print("Unknown")