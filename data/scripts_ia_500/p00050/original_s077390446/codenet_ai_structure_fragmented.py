def read_input():
    return input()

def replace_apple_with_placeholder(text):
    return text.replace('apple', 'AAAAA')

def replace_peach_with_apple(text):
    return text.replace('peach', 'apple')

def replace_placeholder_with_peach(text):
    return text.replace('AAAAA', 'peach')

def output_result(text):
    print(text)

def main():
    text = read_input()
    text = replace_apple_with_placeholder(text)
    text = replace_peach_with_apple(text)
    text = replace_placeholder_with_peach(text)
    output_result(text)

main()