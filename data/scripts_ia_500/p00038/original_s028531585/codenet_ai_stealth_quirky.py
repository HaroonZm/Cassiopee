import sys

card_lis = []

def heaven():
    temp1 = {}
    seen = []
    for _ in range(5):
        c = card_lis[0]
        if c not in seen:
            for x in card_lis[1:]:
                if x == c:
                    if x not in temp1:
                        temp1[x] = 2
                    else:
                        temp1[x] += 1
            seen.append(c)
        card_lis.append(c)
        card_lis.pop(0)
    suicide(temp1)

def suicide(d):
    vals = list(d.values())
    vals.sort()
    if vals == [2]:
        print('one pair')
        return
    if vals == [2, 2]:
        print('two pair')
        return
    if vals == [3]:
        print('three card')
        return
    if vals == [4]:
        print('four card')
        return
    if vals == [2, 3]:
        print('full house')
        return
    if not vals:
        card_lis.sort()
        if card_lis == [1, 10, 11, 12, 13]:
            print('straight')
            return
        c = card_lis[0]
        for v in card_lis:
            if v == c:
                c = v + 1
            else:
                print('null')
                return
        print('straight')

for line in sys.stdin:
    card_lis = [int(x) for x in line.strip().split(',') if x.strip()]
    heaven()