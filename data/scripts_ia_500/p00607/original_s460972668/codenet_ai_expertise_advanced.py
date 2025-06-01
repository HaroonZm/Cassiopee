from sys import stdin

text = []
for line in iter(stdin.readline, "END_OF_TEXT\n"):
    text.append(line.rstrip('\n'))

x = y = 0
buff = ""

for c in iter(lambda: stdin.read(1), '-'):
    if c == 'a':
        x = 0

    elif c == 'e':
        x = len(text[y])

    elif c == 'p':
        if y > 0:
            y -= 1
            x = 0
        else:
            x = 0

    elif c == 'n':
        if y < len(text) - 1:
            y += 1
        x = 0

    elif c == 'f':
        if x < len(text[y]):
            x += 1
        elif y < len(text) - 1:
            y += 1
            x = 0

    elif c == 'b':
        if x > 0:
            x -= 1
        elif y > 0:
            y -= 1
            x = len(text[y])

    elif c == 'd':
        if x < len(text[y]):
            text[y] = text[y][:x] + text[y][x + 1:]
        elif y < len(text) - 1:
            text[y] += text.pop(y + 1)

    elif c == 'k':
        if x < len(text[y]):
            buff, text[y] = text[y][x:], text[y][:x]
        elif y < len(text) - 1:
            text[y] += text.pop(y + 1)
            buff = "\n"
        else:
            buff = ""

    elif c == 'y':
        if buff == "\n":
            new_row = text[y][x:]
            text[y] = text[y][:x]
            text.insert(y + 1, new_row)
            y += 1
            x = 0
        elif buff:
            text[y] = text[y][:x] + buff + text[y][x:]
            x += len(buff)

print(*text, sep="\n")