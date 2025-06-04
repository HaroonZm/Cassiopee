while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    words = []
    for _ in range(n):
        words.extend(input().split())
    k = input()
    freq = {}
    for w in words:
        if w.startswith(k):
            freq[w] = freq.get(w, 0) + 1
    if not freq:
        print("NA")
        continue
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    print(" ".join(w for w, c in sorted_words[:5]))