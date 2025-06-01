from collections import Counter as Cnt

def judge(cards, counts):
    maxc = counts[0][1]
    res = None

    if maxc==4:
        res="four card"
    elif maxc==3:
        res = "full house" if len(counts)>1 and counts[1][1]==2 else "three card"
    elif maxc==2:
        res = "two pair" if len(counts)>1 and counts[1][1]==2 else "one pair"
    else:
        straight1 = cards[0]==1 and cards[1:] == list(range(10,14))
        straight2 = cards == list(range(cards[0], cards[0]+5))
        if straight1 or straight2:
            res = "straight"
        else:
            res = "null"
    return res

class InputReader:
    def __init__(self):
        self.running = True

    def read_line(self):
        if not self.running:
            raise EOFError
        line = input()
        if not line:
            self.running = False
            raise EOFError
        return line

reader = InputReader()

while True:
    try:
        s = reader.read_line()
        cards = sorted(int(x) for x in s.split(","))
    except:
        break
    counts = sorted(Cnt(cards).items(), key=lambda x: -x[1])
    print(judge(cards, counts))