# Your code here!

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
    
    str = []
    for l in range(N):
        str.extend(input().split())

    str.sort()
    k = input()
    words = []

    for i in range(len(str)):
        if str[i][0] == k:
            if len(words) > 0 and words[-1].word == str[i]:
                words[-1].cnt = words[-1].cnt + 1
            else:
                t = Word(str[i],1)
                words.append(t)

    if len(words) == 0:
        print("NA")
    elif len(words) < 5:
        words.sort()
        for i in range(len(words)-1):
            print(words[i].word, end = " ")
        print(words[-1].word)
    else:
        words.sort()
        for i in range(4):
            print(words[i].word, end = " ")
        print(words[4].word)