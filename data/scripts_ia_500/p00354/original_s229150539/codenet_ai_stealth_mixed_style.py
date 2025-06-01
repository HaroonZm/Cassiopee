from datetime import date

def main():
    weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    x = input('Enter day number: ')
    try:
        x = int(x)
    except ValueError:
        print("Invalid input")
        return
    idx = date(2017, 9, x).weekday()
    for i in range(len(weekdays)):
        if i == idx:
            print(weekdays[i])

if __name__ == "__main__":
    main()