def get_input():
    return input()

def get_initial_value():
    return 'Sunny'

def is_sunny(weather):
    return weather == 'Sunny'

def is_cloudy(weather):
    return weather == 'Cloudy'

def get_value_for_sunny():
    return 'Cloudy'

def get_value_for_cloudy():
    return 'Rainy'

def determine_tom(input_str, initial_value):
    if is_sunny(input_str):
        return get_value_for_sunny()
    elif is_cloudy(input_str):
        return get_value_for_cloudy()
    else:
        return initial_value

def output_result(result):
    print(result)

def main():
    user_input = get_input()
    initial_value = get_initial_value()
    tom = determine_tom(user_input, initial_value)
    output_result(tom)

main()