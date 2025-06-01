#!/usr/bin/env python

import sys
import datetime

def get_weekday_name_from_date(month_number, day_number):
    
    weekday_names = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )
    
    date_object = datetime.date(2004, month_number, day_number)
    
    weekday_index = date_object.weekday()
    
    weekday_name = weekday_names[weekday_index]
    
    return weekday_name


def main():
    
    while True:
        
        input_line = sys.stdin.readline()
        
        month_string, day_string = input_line.split(" ")
        
        month_number = int(month_string)
        
        day_number = int(day_string)
        
        if month_number == 0:
            return
        
        weekday_name = get_weekday_name_from_date(month_number, day_number)
        
        print(weekday_name)


if __name__ == '__main__':
    
    main()