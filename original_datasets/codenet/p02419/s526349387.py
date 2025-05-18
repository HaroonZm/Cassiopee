# Problem - 単語の検索

# input
W = input()

# initialization
word_count = 0
is_finish = False

# count
while True:
    word_list = input().split()
    for w in word_list:
        if w=='END_OF_TEXT':
            is_finish = True
            break
        w = w.lower()
        if w==W:
            word_count += 1
    if is_finish:
        break

# output
print(word_count)