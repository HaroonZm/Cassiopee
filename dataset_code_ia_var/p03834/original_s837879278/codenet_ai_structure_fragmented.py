def get_input():
    return input()

def replace_commas(text):
    return text.replace(",", " ")

def print_output(text):
    print(text)

def process():
    user_input = get_input()
    replaced = replace_commas(user_input)
    print_output(replaced)

def main():
    process()

main()