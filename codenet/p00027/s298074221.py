import datetime
import sys

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for line in sys.stdin:
    data = line.strip().split()
    m = data[0]
    d = data[1]
    if m == '0':
        break

    date = datetime.datetime.strptime('2004-' + m + '-' + d + ' 13:13:13', '%Y-%m-%d %H:%M:%S')
    print weekdays[date.weekday()]