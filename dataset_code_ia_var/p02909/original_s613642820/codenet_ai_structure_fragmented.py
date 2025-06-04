def read_input():
    return input()

def is_sunny(s):
    return s == 'Sunny'

def is_cloudy(s):
    return s == 'Cloudy'

def get_next_weather(s):
    if is_sunny(s):
        return "Cloudy"
    elif is_cloudy(s):
        return "Rainy"
    else:
        return "Sunny"

def output_result(result):
    print(result)

def main():
    s = read_input()
    next_weather = get_next_weather(s)
    output_result(next_weather)

main()