from string import lowercase as letters_lowercase
char_count_dict = {letter: 0 for letter in letters_lowercase}
while True:
    try:
        input_line = raw_input()
    except:
        break
    for character in input_line.lower():
        if character in letters_lowercase:
            char_count_dict[character] += 1
for letter in letters_lowercase:
    print letter, ':', char_count_dict[letter]