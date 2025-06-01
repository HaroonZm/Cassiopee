def get_input():
    return input()

def replace_peach_with_placeholder(text):
    return text.replace('peach', 'X')

def replace_apple_with_peach(text):
    return text.replace('apple', 'peach')

def replace_placeholder_with_apple(text):
    return text.replace('X', 'apple')

def main():
    s = get_input()
    s = replace_peach_with_placeholder(s)
    s = replace_apple_with_peach(s)
    s = replace_placeholder_with_apple(s)
    print(s)

main()