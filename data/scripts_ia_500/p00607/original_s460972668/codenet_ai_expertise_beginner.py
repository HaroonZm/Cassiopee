text = []
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    text.append(line)

x = 0
y = 0
buff = ""

while True:
    c = input()
    if c == "-":
        break
    if c == "a":
        x = 0
    elif c == "e":
        x = len(text[y])
    elif c == "p":
        if y == 0:
            x = 0
        else:
            y = y - 1
            x = 0
    elif c == "n":
        if y == len(text) - 1:
            x = 0
        else:
            y = y + 1
            x = 0
    elif c == "f":
        if x < len(text[y]):
            x = x + 1
        else:
            if y < len(text) -1:
                y = y + 1
                x = 0
    elif c == "b":
        if x > 0:
            x = x - 1
        else:
            if y > 0:
                y = y - 1
                x = len(text[y])
    elif c == "d":
        if x < len(text[y]):
            text[y] = text[y][:x] + text[y][x+1:]
        else:
            if y < len(text) -1:
                text[y] = text[y] + text[y+1]
                text.pop(y+1)
    elif c == "k":
        if x < len(text[y]):
            buff = text[y][x:]
            text[y] = text[y][:x]
        else:
            if y < len(text) -1:
                text[y] = text[y] + text[y+1]
                text.pop(y+1)
                buff = "\n"
    elif c == "y":
        if buff == "\n":
            new_line = text[y][x:]
            text[y] = text[y][:x]
            text.insert(y+1, new_line)
            y = y + 1
            x = 0
        else:
            text[y] = text[y][:x] + buff + text[y][x:]
            x = x + len(buff)

for line in text:
    print(line)