W = input()
word_count = 0
is_finish = False

while 1:
    word_list = input().split()
    i = 0
    while i < len(word_list):
        if word_list[i] == 'END_OF_TEXT':
            is_finish = True
            break
        word = word_list[i].lower()
        if word == W:
            word_count += 1
        i += 1
    if is_finish:
        break
print(word_count)