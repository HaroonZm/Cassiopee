def main():
    for _ in range(get_test_cases()):
        s = get_initial_string()
        commands = get_number_of_commands()
        process_commands(s, commands)

def get_test_cases():
    return int(input())

def get_initial_string():
    return input()

def get_number_of_commands():
    return int(input())

def process_commands(s, command_count):
    cur = 0
    commands = read_commands(command_count)
    for command in commands:
        s, cur = handle_command(s, cur, command)
    output_result(s, cur)

def read_commands(command_count):
    return [input() for _ in range(command_count)]

def handle_command(s, cur, command):
    if is_forward_word(command):
        cur = move_forward_word(s, cur)
    elif is_delete_char(command):
        s = delete_char(s, cur)
    elif is_backward_word(command):
        cur = move_backward_word(s, cur)
    elif is_forward_char(command):
        cur = move_forward_char(s, cur)
    elif is_delete_word(command):
        if only_spaces_to_right(s, cur):
            pass
        else:
            s, cur = delete_word(s, cur)
    elif is_insert_string(command):
        to_insert = extract_insert_string(command)
        s, cur = insert_string(s, cur, to_insert)
    else:
        cur = move_backward_char(s, cur)
    return s, cur

def is_forward_word(command):
    return command == 'forward word'

def is_delete_char(command):
    return command == 'delete char'

def is_backward_word(command):
    return command == 'backward word'

def is_forward_char(command):
    return command == 'forward char'

def is_delete_word(command):
    return command == 'delete word'

def is_insert_string(command):
    return command.startswith('i')

def only_spaces_to_right(s, cur):
    return s[cur:].count(' ') == len(s[cur:])

def delete_char(s, cur):
    return s[:cur] + s[cur+1:]

def move_forward_word(s, cur):
    while cur < len(s) and s[cur] == ' ':
        cur += 1
    while cur < len(s) and s[cur] != ' ':
        cur += 1
    return cur

def move_backward_word(s, cur):
    while cur > 0 and s[cur-1] == ' ':
        cur -= 1
    while cur > 0 and s[cur-1] != ' ':
        cur -= 1
    return cur

def move_forward_char(s, cur):
    return min(len(s), cur + 1)

def move_backward_char(s, cur):
    return max(0, cur - 1)

def delete_word(s, cur):
    start_cur = cur
    while cur < len(s) and s[cur] == ' ':
        s = s[:cur] + s[cur+1:]
    while cur < len(s) and s[cur] != ' ':
        s = s[:cur] + s[cur+1:]
    return s, start_cur

def extract_insert_string(command):
    return command.split('"')[1]

def insert_string(s, cur, to_insert):
    s = s[:cur] + to_insert + s[cur:]
    cur += len(to_insert)
    return s, cur

def output_result(s, cur):
    print(s[:cur] + '^' + s[cur:])

main()