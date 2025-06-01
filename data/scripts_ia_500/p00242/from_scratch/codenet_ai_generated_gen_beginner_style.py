while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    words = []
    for _ in range(n):
        line = input()
        words += line.split()
    k = input()
    freq = {}
    for w in words:
        if w.startswith(k):
            freq[w] = freq.get(w, 0) + 1
    if not freq:
        print("NA")
    else:
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        result = [w for w, c in sorted_words[:5]]
        print(' '.join(result))