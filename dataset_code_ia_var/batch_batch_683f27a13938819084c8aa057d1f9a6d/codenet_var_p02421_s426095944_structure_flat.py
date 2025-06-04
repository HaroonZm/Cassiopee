n = int(input())
taro = 0
hana = 0
i = 0
while i < n:
    cards = input().split()
    taro_c = cards[0]
    hana_c = cards[1]
    if taro_c > hana_c:
        taro = taro + 3
    elif hana_c > taro_c:
        hana = hana + 3
    else:
        taro = taro + 1
        hana = hana + 1
    i = i + 1
print(taro, hana)