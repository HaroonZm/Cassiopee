d = {}
while True:
    try:
        line = input()
        if not line:
            break
        parts = line.split()
        word = parts[0]
        page = int(parts[1])
        if word in d:
            d[word].append(page)
        else:
            d[word] = [page]
    except EOFError:
        break

for word in sorted(d.keys()):
    pages = d[word]
    pages.sort()
    print(word)
    print(' '.join(str(p) for p in pages))