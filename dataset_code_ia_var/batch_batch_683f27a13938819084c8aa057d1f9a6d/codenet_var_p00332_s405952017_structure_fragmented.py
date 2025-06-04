def get_input():
    return input()

def parse_input(inp):
    return map(int, inp.split())

def main():
    e, y = parse_input(get_input())
    if is_wareki(e):
        print(wareki(y))
    else:
        print(seireki(e, y))

def is_wareki(e):
    return e == 0

def wareki(year):
    if is_meiji(year):
        return meiji(year)
    elif is_taisho(year):
        return taisho(year)
    elif is_showa(year):
        return showa(year)
    else:
        return heisei(year)

def is_meiji(year):
    return year <= 1911

def meiji(year):
    return concat("M", year - 1867)

def is_taisho(year):
    return year <= 1925

def taisho(year):
    return concat("T", year - 1911)

def is_showa(year):
    return year <= 1988

def showa(year):
    return concat("S", year - 1925)

def heisei(year):
    return concat("H", year - 1988)

def concat(prefix, num):
    return prefix + str(num)

def seireki(e, y):
    if is_e1(e):
        return seireki_e1(y)
    elif is_e2(e):
        return seireki_e2(y)
    elif is_e3(e):
        return seireki_e3(y)
    else:
        return seireki_default(y)

def is_e1(e):
    return e == 1

def is_e2(e):
    return e == 2

def is_e3(e):
    return e == 3

def seireki_e1(y):
    return y + 1867

def seireki_e2(y):
    return y + 1911

def seireki_e3(y):
    return y + 1925

def seireki_default(y):
    return y + 1988

main()