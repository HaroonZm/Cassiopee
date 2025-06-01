import re

text = input()
words = re.split(r'\s|"|,|\.', text)
result = []

for word in words:
    if len(word) > 2 and len(word) < 7:
        result.append(word)

print(*result)