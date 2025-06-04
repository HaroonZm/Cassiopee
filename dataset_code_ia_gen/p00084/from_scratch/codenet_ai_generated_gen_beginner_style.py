line = input()

separators = [' ', '.', ',']
for sep in separators:
    line = line.replace(sep, ' ')

words = line.split()
result = []
for w in words:
    if 3 <= len(w) <= 6:
        result.append(w)

print(' '.join(result))