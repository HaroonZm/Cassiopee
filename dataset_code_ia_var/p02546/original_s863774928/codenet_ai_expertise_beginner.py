word = input()

last_letter = word[len(word)-1]

if last_letter == "s":
    print(word + "es")
else:
    print(word + "s")