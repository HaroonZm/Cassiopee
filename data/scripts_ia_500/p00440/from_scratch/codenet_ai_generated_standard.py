import sys
input = sys.stdin.readline

while True:
    n,k = map(int, input().split())
    if n == 0 and k == 0:
        break
    cards = [int(input()) for _ in range(k)]
    has_blank = cards.count(0) > 0
    card_set = set(c for c in cards if c != 0)
    max_len = 0
    visited = set()
    for c in card_set:
        if c-1 not in card_set:
            start = c
            length = 0
            while start + length in card_set:
                length += 1
            if has_blank:
                # try extend length with blank card inside range
                # check gaps inside sequence - fill one gap with blank
                # since only one blank, we can increase length by 1 if gap exists
                max_len = max(max_len, length+1 if length < n else length)
            else:
                max_len = max(max_len, length)
    # if has blank but no cards, max length is 1
    if has_blank and max_len == 0:
        max_len = 1
    print(max_len)