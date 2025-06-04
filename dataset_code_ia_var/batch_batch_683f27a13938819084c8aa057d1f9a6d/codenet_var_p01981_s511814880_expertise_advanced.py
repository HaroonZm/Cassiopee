from sys import exit, stdin

def process_dates(lines):
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            exit()
        year, month, day, *rest = line.split()
        y, m, d = int(year), int(month), int(day)
        if m > 31 or (m == 31 and d >= 5):
            print(f'? {m-30} {d} {" ".join(rest)}')
        else:
            print(line)

if __name__ == "__main__":
    from itertools import islice
    process_dates(islice(stdin, 102))