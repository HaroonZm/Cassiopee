def get_input():
    return input()

def extract_prefix(text):
    return text[:3]

def display_result(result):
    print(result)

def main():
    user_input = get_input()
    prefix = extract_prefix(user_input)
    display_result(prefix)

main()