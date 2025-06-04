text = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    text.append(s)

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
        if y < len(text) - 1:
            y = y + 1
            x = 0
        else:
            x = 0
    elif c == "f":
        if x < len(text[y]):
            x = x + 1
        else:
            if y < len(text) - 1:
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
            # Delete character at position x
            line = list(text[y])
            del line[x]
            text[y] = ''.join(line)
        else:
            if y < len(text) - 1:
                # Join with next line
                text[y] = text[y] + text[y + 1]
                del text[y + 1]
    elif c == "k":
        if x < len(text[y]):
            buff = text[y][x:]
            text[y] = text[y][:x]
        else:
            if y < len(text) - 1:
                text[y] = text[y] + text[y + 1]
                del text[y + 1]
                buff = "\n"
    elif c == "y":
        if buff == "\n":
            line_rest = text[y][x:]
            text[y] = text[y][:x]
            text.insert(y + 1, line_rest)
            x = 0
            y = y + 1
        else:
            text[y] = text[y][:x] + buff + text[y][x:]
            x = x + len(buff)

for line in text:
    print(line)