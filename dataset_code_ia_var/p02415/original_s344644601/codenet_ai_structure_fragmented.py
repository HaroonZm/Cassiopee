def get_input():
    return input()

def convert_to_list(s):
    return list(s)

def is_upper(char):
    return char.isupper()

def to_lower(char):
    return char.lower()

def to_upper(char):
    return char.upper()

def process_char(char):
    if is_upper(char):
        return to_lower(char)
    else:
        return to_upper(char)

def process_list(S):
    result = []
    for i in range(len(S)):
        converted = process_char(S[i])
        result.append(converted)
    return result

def join_list(lst):
    return ''.join(lst)

def main():
    s = get_input()
    S = convert_to_list(s)
    new_S = process_list(S)
    output = join_list(new_S)
    print(output)

main()