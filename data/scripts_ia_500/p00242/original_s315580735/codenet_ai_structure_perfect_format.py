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
    str_list = []
    for _ in range(N):
        str_list.extend(input().split())
    str_list.sort()
    k = input()
    words = []
    for i in range(len(str_list)):
        if str_list[i][0] == k:
            if len(words) > 0 and words[-1].word == str_list[i]:
                words[-1].cnt += 1
            else:
                words.append(Word(str_list[i], 1))
    if len(words) == 0:
        print("NA")
    else:
        words.sort()
        limit = min(5, len(words))
        for i in range(limit - 1):
            print(words[i].word, end=" ")
        print(words[limit - 1].word)