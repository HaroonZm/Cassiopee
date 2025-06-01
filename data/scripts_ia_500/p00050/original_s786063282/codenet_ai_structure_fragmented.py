def read_input():
    return raw_input()

def replace_apple_with_placeholder(s):
    return s.replace("apple", "xxxxx")

def replace_peach_with_apple(s):
    return s.replace("peach", "apple")

def replace_placeholder_with_peach(s):
    return s.replace("xxxxx", "peach")

def main():
    s = read_input()
    s = replace_apple_with_placeholder(s)
    s = replace_peach_with_apple(s)
    s = replace_placeholder_with_peach(s)
    print s

main()