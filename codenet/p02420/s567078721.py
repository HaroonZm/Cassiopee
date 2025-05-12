while True:
    cards=input()
    if cards=='-': break
    for _ in range(int(input())):
        h = int(input())
        cards=cards[h:]+cards[:h]
    print(cards)