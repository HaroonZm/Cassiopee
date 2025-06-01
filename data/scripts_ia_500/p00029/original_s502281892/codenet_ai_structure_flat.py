word_l = input().split()
dic = {}
for w in word_l:
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1
max_len = 0
longest_word = ''
max_count = 0
most_frequent_word = ''
for w in word_l:
    if len(w) > max_len:
        max_len = len(w)
        longest_word = w
for w, c in dic.items():
    if c > max_count:
        max_count = c
        most_frequent_word = w
print(most_frequent_word, longest_word)