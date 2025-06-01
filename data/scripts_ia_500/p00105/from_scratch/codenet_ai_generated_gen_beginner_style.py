pages = {}
while True:
    try:
        line = input()
        if not line:
            break
        word, page = line.split()
        page = int(page)
        if word not in pages:
            pages[word] = []
        if page not in pages[word]:
            pages[word].append(page)
    except EOFError:
        break

for word in sorted(pages.keys()):
    pages[word].sort()
    print(word)
    print(" ".join(str(p) for p in pages[word]))