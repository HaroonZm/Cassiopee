letters = "abcdefghijklmnopqrstuvwxyz"
user_input = input()
different_letters = []

for letter in letters:
    if letter not in user_input:
        different_letters.append(letter)

if len(different_letters) == 0:
    print("None")
else:
    different_letters.sort()
    print(different_letters[0])