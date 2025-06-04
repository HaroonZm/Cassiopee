import collections

while True:
    try:
        card = list(map(int, input().split(",")))
    except:
        break
    cnt = collections.Counter(card)
    sorted_card = sorted(card)
    cnt_items = sorted(cnt.items(), key=lambda x: -x[1])
    nmax = cnt_items[0][1]
    result = ""
    if nmax == 4:
        result = "four card"
    elif nmax == 3:
        if cnt_items[1][1] == 2:
            result = "full house"
        else:
            result = "three card"
    elif nmax == 2:
        if cnt_items[1][1] == 2:
            result = "two pair"
        else:
            result = "one pair"
    elif (sorted_card[0] == 1 and list(range(10, 14)) == sorted_card[1:]) or list(range(sorted_card[0], sorted_card[0] + 5)) == sorted_card:
        result = "straight"
    else:
        result = "null"
    print(result)