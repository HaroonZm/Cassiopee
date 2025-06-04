def get_input():
    return input()

def to_int(value):
    return int(value)

def get_n():
    value = get_input()
    return to_int(value)

def get_single_list_element():
    value = get_input()
    return to_int(value)

def collect_elements(count):
    items = []
    for _ in range(count):
        items.append(get_single_list_element())
    return items

def is_even(number):
    return number % 2 == 0

def all_even(numbers):
    return all(is_even(x) for x in numbers)

def decision_text(is_all_even):
    if is_all_even:
        return 'second'
    else:
        return 'first'

def main():
    n = get_n()
    a = collect_elements(n)
    result = all_even(a)
    text = decision_text(result)
    print(text)

main()