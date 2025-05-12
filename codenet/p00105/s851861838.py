import sys

dictionary = dict()

for line in sys.stdin.readlines():
    line = line.strip()
    word, num = line.split()
    if not dictionary.has_key(word):
        dictionary[word] = list()
    dictionary[word].append(int(num))

for key in sorted(dictionary.keys()):
    print key
    print " ".join(map(str, sorted(dictionary[key])))