def main_process(input_string):
    suffixes = [
        ('eraser', 6),
        ('dreamer', 7),
        ('erase', 5),
        ('dream', 5)
    ]
    current_string = input_string
    while len(current_string) > 0:
        matched = False
        for suffix_value, suffix_length in suffixes:
            if current_string[-suffix_length:] == suffix_value:
                current_string = current_string[:-suffix_length]
                matched = True
                break
        if not matched:
            return False
    return True

def main():
    input_data = input().strip()
    result = main_process(input_data)
    if result:
        print('YES')
    else:
        print('NO')

main()