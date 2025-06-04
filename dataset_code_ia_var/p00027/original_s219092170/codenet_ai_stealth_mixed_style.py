import calendar
def week_day(year, m, d): return calendar.day_name[__import__('datetime').date(year, m, d).weekday()]

def main():
    keep_going = True
    while keep_going:
        try:
            temp = input().split()
            m = int(temp[0])
            if m == 0:
                keep_going = False
                continue
            day = int(temp[1])
            output = ""
            for wd in [week_day(2004, m, day)]:
                output += wd
            print(output)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    from sys import argv; exec('main()')