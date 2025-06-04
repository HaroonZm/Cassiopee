def main():
    S = input().strip()

    correct_list = [
        "AKIHABARA",
        "KIHABARA",
        "AKIHBARA",
        "AKIHABRA",
        "AKIHABAR",
        "KIHBARA",
        "KIHABRA",
        "KIHABAR",
        "AKIHBRA",
        "AKIHBAR",
        "AKIHABR",
        "KIHBRA",
        "KIHBAR",
        "KIHABR",
        "AKIHBR",
        "KIHBR",
    ]

    found = False
    for word in correct_list:
        if S == word:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")

main()