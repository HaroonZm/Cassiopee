def get_input():
    return input()

def is_sunny(s):
    return s == 'Sunny'

def is_rainy(s):
    return s == 'Rainy'

def print_cloudy():
    print('Cloudy')

def print_sunny():
    print('Sunny')

def print_rainy():
    print('Rainy')

def process_weather(s):
    if is_sunny(s):
        print_cloudy()
    elif is_rainy(s):
        print_sunny()
    else:
        print_rainy()

def main():
    s = get_input()
    process_weather(s)

main()