for idx_input_line in range(102):
    raw_input_str = input()
    if raw_input_str.startswith('#'):
        exit()
    date_components = raw_input_str.split()
    year_val = int(date_components[1])
    month_val = int(date_components[2])
    other_val = date_components[3]
    if year_val > 31:
        adj_year_val = year_val - 30
        print(f'? {adj_year_val} {month_val} {other_val}')
        continue
    if year_val == 31 and month_val >= 5:
        adj_year_val = year_val - 30
        print(f'? {adj_year_val} {month_val} {other_val}')
        continue
    print(' '.join(date_components))