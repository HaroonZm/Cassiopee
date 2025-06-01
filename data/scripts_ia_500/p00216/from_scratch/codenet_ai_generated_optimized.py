BASIC_CHARGE = 1150
PREV_FEE = 4280

def water_fee(w):
    fee = BASIC_CHARGE
    if w > 30:
        fee += (w - 30) * 160
        w = 30
    if w > 20:
        fee += (w - 20) * 140
        w = 20
    if w > 10:
        fee += (w - 10) * 125
    return fee

while True:
    w = int(input())
    if w == -1:
        break
    print(PREV_FEE - water_fee(w))