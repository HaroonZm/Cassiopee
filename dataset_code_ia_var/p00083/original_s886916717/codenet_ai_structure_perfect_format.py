import sys
from datetime import date

f = sys.stdin

eras = {
    'pre-meiji': {'start': None, 'end': date(1868, 9, 7)},
    'meiji':     {'start': date(1868, 9, 8),  'end': date(1912, 7, 29)},
    'taisho':    {'start': date(1912, 7, 30), 'end': date(1926, 12, 24)},
    'showa':     {'start': date(1926, 12, 25), 'end': date(1989, 1, 7)},
    'heisei':    {'start': date(1989, 1, 8),   'end': None}
}

for line in f:
    y, m, d = map(int, line.split())
    target = date(y, m, d)
    for era_name, period in eras.items():
        start_ok = period['start'] is None or period['start'] <= target
        end_ok = period['end'] is None or target <= period['end']
        if start_ok and end_ok:
            if era_name == 'pre-meiji':
                print(era_name)
            else:
                print(era_name, target.year - period['start'].year + 1, target.month, target.day)
            break