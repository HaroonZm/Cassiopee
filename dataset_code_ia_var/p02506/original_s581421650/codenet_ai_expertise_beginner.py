word = raw_input().lower()
words = []
while True:
    line = raw_input()
    if line == "END_OF_TEXT":
        break
    line_words = line.lower().split()
    for w in line_words:
        words.append(w)
count = 0
for w in words:
    if w == word:
        count += 1
print(count)