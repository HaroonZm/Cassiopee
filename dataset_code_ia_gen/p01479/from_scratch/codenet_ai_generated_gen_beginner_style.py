s = input()

# 分割する単語
words = []
i = 0
while i < len(s):
    if s[i:i+3] == "egg":
        words.append("egg")
        i += 3
    else:
        # chickenは7文字
        words.append("chicken")
        i += 7

# 文ごとに分割（同じ単語が連続したら区切り）
sentences = []
current_sentence = [words[0]]
for i in range(1, len(words)):
    if words[i] == words[i-1]:
        sentences.append(current_sentence)
        current_sentence = [words[i]]
    else:
        current_sentence.append(words[i])
sentences.append(current_sentence)

# 各文の先頭単語を集める
first_words = []
for sentence in sentences:
    first_words.append(sentence[0])

# 最初に出てくる単語が答え
print(first_words[0])