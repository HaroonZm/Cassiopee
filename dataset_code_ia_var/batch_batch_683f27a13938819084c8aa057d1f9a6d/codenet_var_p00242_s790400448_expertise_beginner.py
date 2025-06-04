BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001

class Info:
    def __init__(self, arg_word, arg_count):
        self.word = arg_word
        self.count = arg_count

    def __lt__(self, another):
        if self.count != another.count:
            return self.count > another.count
        else:
            return self.word < another.word

while True:
    num_row = int(input())
    if num_row == 0:
        break

    DICT = {}
    rev_DICT = {}
    COUNT = {}
    num_words = 0

    for _ in range(num_row):
        words = input().split()
        for word in words:
            if word in DICT:
                COUNT[DICT[word]] += 1
            else:
                DICT[word] = num_words
                rev_DICT[num_words] = word
                num_words += 1
                COUNT[DICT[word]] = 1

    head_word = input()
    table = []
    for i in range(num_words):
        word = rev_DICT[i]
        if word[0] != head_word:
            continue
        table.append(Info(word, COUNT[DICT[word]]))

    if len(table) == 0:
        print("NA")
        continue

    table.sort()
    print(table[0].word, end="")
    for i in range(1, min(5, len(table))):
        print(" " + table[i].word, end="")
    print()