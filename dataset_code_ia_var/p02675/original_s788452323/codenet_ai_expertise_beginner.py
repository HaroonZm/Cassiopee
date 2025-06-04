import sys

def solve():
    n = input()
    last_char = n[-1]
    if last_char == "2" or last_char == "4" or last_char == "5" or last_char == "7" or last_char == "9":
        print("hon")
    elif last_char == "0" or last_char == "1" or last_char == "6" or last_char == "8":
        print("pon")
    else:
        print("bon")

if __name__ == "__main__":
    solve()