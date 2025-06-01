def read_input():
    return input()

def replace_apple_with_placeholder(text):
    return text.replace('apple', '___')

def replace_peach_with_apple(text):
    return text.replace('peach', 'apple')

def replace_placeholder_with_peach(text):
    return text.replace('___', 'peach')

def main():
    x = read_input()
    x = replace_apple_with_placeholder(x)
    x = replace_peach_with_apple(x)
    x = replace_placeholder_with_peach(x)
    print(x)

main()