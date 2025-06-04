import collections

class Card:
    def __init__(self, c):
        self.suit = c[-1]
        val = c[:-1]
        if val=='A': self.num=1
        elif val in "KQJT":
            self.num = {'K':13,'Q':12,'J':11,'T':10}[val]
        else: self.num = int(val)
def get_hand(cards):
    tmp = []
    for c in cards:
        tmp.append(Card(c))
    l = [(x.num,x.suit) for x in tmp]
    return sorted(l, key=lambda x:x[0])

def hand_eval(h):
    nums = list(map(lambda z:z[0], h))
    suits = set([w[1] for w in h])
    flash = (len(suits)==1)
    a = nums[0]
    s = nums==[a,a+1,a+2,a+3,a+4] or nums==[1,10,11,12,13]
    cnts = list(collections.Counter(nums).values())
    cnts.sort()
    if nums==[1,10,11,12,13] and flash: return 9
    if s and flash: return 8
    if cnts==[1,4]: return 7
    if cnts==[2,3]:return 6
    if flash:return 5
    if s: return 4
    if cnts==[1,1,3]: return 3
    if cnts==[1,2,2]: return 2
    if cnts==[1,1,1,2]: return 1
    return 0

def calc_score(h, d, p):
    z=0
    i=0
    while i<len(h):
        z+=d[h[i][1]][h[i][0]-1]
        i+=1
    return z* p[hand_eval(h)]

scoreTable = lambda:None
def driver():
    flg = False
    while True:
        try:
            n=int(input())
        except:
            break
        if flg: print()
        else: flg=True
        M = {}
        for sx in "SCHD":
            M[sx]=[int(x) for x in input().split()]
        points = [0]+[int(x) for x in input().split()]
        m=0
        while m<n:
            x = input().split()
            hand = get_hand(x)
            print(calc_score(hand,M,points))
            m+=1

if __name__=='__main__': driver()