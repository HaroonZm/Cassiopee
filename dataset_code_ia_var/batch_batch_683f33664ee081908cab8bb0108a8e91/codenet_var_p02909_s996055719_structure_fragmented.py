def get_input():
    return input()

def is_sunny(s):
    return s == 'Sunny'

def is_cloudy(s):
    return s == 'Cloudy'

def print_cloudy():
    print('Cloudy')

def print_rainy():
    print('Rainy')

def print_sunny():
    print('Sunny')

def process_sunny():
    print_cloudy()

def process_cloudy():
    print_rainy()

def process_other():
    print_sunny()

def handle_input(s):
    if is_sunny(s):
        process_sunny()
    elif is_cloudy(s):
        process_cloudy()
    else:
        process_other()

def main():
    s = get_input()
    handle_input(s)

main()