def read_input():
    return input()

def replace_apple_with_kunimatsu(text):
    return text.replace("apple", "kunimatsu")

def replace_peach_with_apple(text):
    return text.replace("peach", "apple")

def replace_kunimatsu_with_peach(text):
    return text.replace("kunimatsu", "peach")

def main():
    text = read_input()
    text = replace_apple_with_kunimatsu(text)
    text = replace_peach_with_apple(text)
    text = replace_kunimatsu_with_peach(text)
    print(text)

main()