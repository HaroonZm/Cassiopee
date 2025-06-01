table = {
    11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'e',
    21: 'f', 22: 'g', 23: 'h', 24: 'i', 25: 'j',
    31: 'k', 32: 'l', 33: 'm', 34: 'n', 35: 'o',
    41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    51: 'u', 52: 'v', 53: 'w', 54: 'x', 55: 'y',
    61: 'z', 62: '.', 63: '?', 64: '!', 65: ' '
}

while True:
    mes = input()
    if mes == "":
        break
    result = ""
    is_valid = True
    i = 0
    while i < len(mes):
        pair = mes[i:i+2]
        if len(pair) < 2:
            is_valid = False
            break
        number = int(pair)
        if number in table:
            result += table[number]
        else:
            is_valid = False
            break
        i += 2
    if is_valid:
        print(result)
    else:
        print("NA")