import datetime
import sys


list_of_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


for input_line in sys.stdin:

    stripped_line = input_line.strip()

    splitted_data = stripped_line.split()

    month_string = splitted_data[0]

    day_string = splitted_data[1]

    if month_string == '0':

        break

    date_string = '2004-' + month_string + '-' + day_string + ' 13:13:13'

    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    weekday_index = date_object.weekday()

    weekday_name = list_of_weekdays[weekday_index]

    print(weekday_name)