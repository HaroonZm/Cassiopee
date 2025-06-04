while True:
    n = input()
    if n == 0:
        break
    word_count = {}
    for i in range(n):
        line = raw_input().split()
        for word in line:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    alpha = raw_input()
    result = []
    items = list(word_count.items())
    # Sort alphabetically first
    items.sort()
    # Then sort by count descending
    items.sort(key=lambda x: x[1], reverse=True)
    for word, count in items:
        if word.startswith(alpha):
            result.append(word)
    if len(result) > 0:
        print " ".join(result)
    else:
        print "NA"