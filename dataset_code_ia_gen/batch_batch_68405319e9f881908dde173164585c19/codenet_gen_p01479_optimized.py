import sys
sys.setrecursionlimit(10**7)

def parse_words(s):
    words = []
    i = 0
    while i < len(s):
        if s.startswith("egg", i):
            words.append("egg")
            i += 3
        else:
            words.append("chicken")
            i += 7
    return words

def split_documents(words):
    docs = []
    start = 0
    for i in range(1, len(words)):
        if words[i] == words[i-1]:
            docs.append(words[start:i])
            start = i
    docs.append(words[start:])
    return docs

def solve(s):
    words = parse_words(s)
    docs = split_documents(words)

    n = len(docs)

    # Build partial order graph between documents according to first words
    # same era means first words of docs share relations, and their pairs belong to same era
    # Use indices of docs to determine order
    # If first word of doc i comes before first word of doc j in the original string, then doc i < doc j

    # According to the statement, the order of eras is the order of documents
    # The parent-child relation is that each document's first word was born same era
    # The problem reduces to merging the words and deducing which came first

    # The first word of the first document is earliest born among first words of all documents
    # From the rules, the first words of docs 0..n-1 are born same era, ordered by order in docs
    # The first word of the first document is "earliest" among those first words
    # And their parents are the second words of each doc which correspond to the rest

    # Key is the first word of first document is the earliest word born

    # Hence, the output is the first word of the first document.

    return docs[0][0]

s = input().strip()
print(solve(s))