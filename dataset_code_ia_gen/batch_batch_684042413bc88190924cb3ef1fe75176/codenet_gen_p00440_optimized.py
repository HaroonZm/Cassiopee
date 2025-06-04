import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    cards = [int(input()) for _ in range(k)]
    blank = cards.count(0)
    cards_set = set(x for x in cards if x != 0)
    arr = sorted(cards_set)
    max_len = 0
    left = 0
    for right in range(len(arr)):
        # nombre de nombres manquants entre arr[left] et arr[right]
        need = arr[right] - arr[left] + 1 - (right - left + 1)
        while need > blank:
            left += 1
            need = arr[right] - arr[left] + 1 - (right - left + 1)
        cur_len = (right - left + 1) + blank
        if cur_len > max_len:
            max_len = cur_len
    if max_len > n:
        max_len = n
    print(max_len)