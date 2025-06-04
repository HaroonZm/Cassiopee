def get_input():
    try:
        return raw_input()
    except:
        return None

def find_at_symbol(s):
    return "@" in s

def get_at_index(s):
    return s.index("@")

def append_before_at(ans, s):
    idx = get_at_index(s)
    return ans + s[0:idx], s[idx:]

def process_at_sequence(s):
    repeat_count = int(s[1])
    repeat_char = s[2]
    rest = s[3:]
    return repeat_char * repeat_count + rest

def process_string(char):
    ans = ""
    while find_at_symbol(char):
        ans, char = append_before_at(ans, char)
        char = process_at_sequence(char)
    ans += char
    return ans

def print_result(ans):
    print ans

def main_loop():
    while True:
        char = get_input()
        if char is None:
            break
        ans = process_string(char)
        print_result(ans)

main_loop()