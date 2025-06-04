import sys

dictionary = {}

for line in sys.stdin.readlines():
    line = line.strip()
    word, num = line.split()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(int(num))

for key in sorted(dictionary.keys()):
    print(key)
    print(" ".join(map(str, sorted(dictionary[key]))))