from datetime import date, timedelta

def read_input():
    return input()

def is_termination_signal(s):
    return s == '#'

def parse_input(s):
    return list(map(int, s.split('.')))

def count_400_year_chunks(year):
    chunks = 0
    while year > 3000:
        year -= 400
        chunks += 1
    return year, chunks

def days_in_400_years():
    return 365 * 400 + 97

def calculate_days_from_date(d, st):
    year, chunks = count_400_year_chunks(d[0])
    adjustment = chunks * days_in_400_years()
    ed = create_date(year, d[1], d[2])
    days_diff = calculate_days_difference(ed, st)
    return adjustment + days_diff

def create_date(y, m, d):
    return date(y, m, d)

def calculate_days_difference(d1, d2):
    return (d1 - d2).days

def calculate_mayan_date_components(total_days):
    ki = total_days % 20
    total_days //= 20
    w = total_days % 18
    total_days //= 18
    t = total_days % 20
    total_days //= 20
    ka = total_days % 20
    total_days //= 20
    b = total_days % 13
    return b, ka, t, w, ki

def format_mayan_date(b, ka, t, w, ki):
    return f"{b}.{ka}.{t}.{w}.{ki}"

def mayan_to_days(d):
    r = 0
    r = add_component(r, d[0], 20)
    r = add_component(r, d[1], 20)
    r = add_component(r, d[2], 18)
    r = add_component(r, d[3], 20)
    r = add_component(r, d[4], 1)
    return r

def add_component(current, value, multiplier):
    return current * multiplier + value

def days_to_date(days, st):
    return st + timedelta(days=days)

def format_gregorian_date(d):
    return f"{d.year}.{d.month}.{d.day}"

def process_gregorian_to_mayan(d, st):
    total_days = calculate_days_from_date(d, st)
    b, ka, t, w, ki = calculate_mayan_date_components(total_days)
    return format_mayan_date(b, ka, t, w, ki)

def process_mayan_to_gregorian(d, st):
    total_days = mayan_to_days(d)
    ed = days_to_date(total_days, st)
    return format_gregorian_date(ed)

def main():
    st = date(2012, 12, 21)
    while True:
        s = read_input()
        if is_termination_signal(s):
            break
        d = parse_input(s)
        if len(d) == 3:
            output = process_gregorian_to_mayan(d, st)
            print(output)
        else:
            output = process_mayan_to_gregorian(d, st)
            print(output)

main()