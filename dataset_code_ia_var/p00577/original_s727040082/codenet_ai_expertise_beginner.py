def found_min(x, y):
    if x == -1 and y == -1:
        return -1
    if x == -1:
        return y
    if y == -1:
        return x
    if x < y:
        return x
    else:
        return y

n = int(input())
Stamp = input()

OXStamp = 0
index = 0

while True:
    pos1 = Stamp[index:].find("OX")
    pos2 = Stamp[index:].find("XO")
    i = found_min(pos1, pos2)
    if i == -1:
        break
    OXStamp += 1
    index = index + i + 2
print(OXStamp)