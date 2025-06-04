kan_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"]

# set for quick checking two-letter Kan-characters
two_letter = set(["ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"])

# read number of lines
n = int(input())

# initialize counts: for each Kan-character, store dictionary of following Kan-chars counts
counts = {}
for kc in kan_chars:
    counts[kc] = {}
    for kc2 in kan_chars:
        counts[kc][kc2] = 0

for _ in range(n):
    line = input()
    words = line.split()
    for word in words:
        # parse word into Kan-characters from left to right, longest match first
        parsed = []
        i = 0
        while i < len(word):
            if i+1 < len(word):
                pair = word[i:i+2]
                if pair in two_letter:
                    parsed.append(pair)
                    i += 2
                    continue
            # otherwise single letter
            parsed.append(word[i])
            i += 1
        # count pairs in parsed word
        for i in range(len(parsed)-1):
            c1 = parsed[i]
            c2 = parsed[i+1]
            counts[c1][c2] += 1

# for each Kan-character, find the most frequent following Kan-character, or 'a' and 0 if none
for kc in kan_chars:
    max_count = 0
    max_kc2 = "a"
    for kc2 in kan_chars:
        if counts[kc][kc2] > max_count:
            max_count = counts[kc][kc2]
            max_kc2 = kc2
    print(kc, max_kc2, max_count)