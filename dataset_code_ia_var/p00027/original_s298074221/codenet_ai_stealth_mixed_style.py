from datetime import datetime
import sys

def get_weekday(m, d):
    # Utilisation en mode fonctionnel (map, lambda)
    date_str = '-'.join(map(lambda x: str(x).zfill(2), ['2004', m, d])) + ' 13:13:13'
    wkdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return wkdays[dt.weekday()]

class StopProcessing(Exception): pass

try:
    while True:
        l = sys.stdin.readline()
        if not l:
            break
        parts = l.strip().split()
        if len(parts) < 2 or parts[0] == '0': raise StopProcessing()
        mth, day = parts[0], parts[1]
        result = get_weekday(mth, day)
        # Style procédural ; print façon Python 3 et suppression parenthèses
        print(result)
except StopProcessing:
    pass