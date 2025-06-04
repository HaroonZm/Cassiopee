class Word:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        if self.cnt == other.cnt:
            return self.word < other.word
        else:
            return self.cnt > other.cnt

while True:
    N = int(input())
    if N == 0:
        break

    all_words = []
    for i in range(N):
        line = input()
        words_in_line = line.split()
        for word in words_in_line:
            all_words.append(word)
    all_words.sort()

    first_letter = input()
    word_objs = []

    for word in all_words:
        if word[0] == first_letter:
            found = False
            for w in word_objs:
                if w.word == word:
                    w.cnt += 1
                    found = True
                    break
            if not found:
                word_objs.append(Word(word, 1))

    if len(word_objs) == 0:
        print("NA")
    else:
        word_objs.sort()
        if len(word_objs) < 5:
            for i in range(len(word_objs)):
                print(word_objs[i].word, end='')
                if i != len(word_objs)-1:
                    print(" ", end='')
            print()
        else:
            for i in range(5):
                print(word_objs[i].word, end='')
                if i != 4:
                    print(" ", end='')
            print()