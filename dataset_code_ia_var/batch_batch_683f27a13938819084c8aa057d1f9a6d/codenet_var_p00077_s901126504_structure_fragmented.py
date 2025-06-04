def get_input():
    try:
        return input()
    except:
        return None

def is_at_symbol(char):
    return char == "@"

def get_repetition_count(string, i):
    return int(string[i+1])

def get_repetition_character(string, i):
    return string[i+2]

def process_at_sequence(string, i):
    count = get_repetition_count(string, i)
    char = get_repetition_character(string, i)
    return char * count

def increment_index_at(i):
    return i + 3

def increment_index_default(i):
    return i + 1

def process_character(ans, char):
    return ans + char

def end_of_string(i, string):
    return i >= len(string)

def process_string(string):
    ans = ""
    i = 0
    while not end_of_string(i, string):
        if is_at_symbol(string[i]):
            ans += process_at_sequence(string, i)
            i = increment_index_at(i)
        else:
            ans = process_character(ans, string[i])
            i = increment_index_default(i)
    return ans

def main_loop():
    while True:
        string = get_input()
        if string is None:
            break
        ans = process_string(string)
        print(ans)

main_loop()