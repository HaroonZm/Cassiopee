from sys import stdin

def process():
    from itertools import islice
    text = list(iter(lambda: input(), "END_OF_TEXT"))

    x, y, buff = 0, 0, ""
    cmds = iter(input, "-")

    for c in cmds:
        match c:
            case "a":
                x = 0
            case "e":
                x = len(text[y])
            case "p":
                if y > 0:
                    y -= 1
                x = 0
            case "n":
                if y < len(text) - 1:
                    y += 1
                x = 0
            case "f":
                if x < len(text[y]):
                    x += 1
                elif y < len(text) - 1:
                    y += 1
                    x = 0
            case "b":
                if x > 0:
                    x -= 1
                elif y > 0:
                    y -= 1
                    x = len(text[y])
            case "d":
                if x < len(text[y]):
                    text[y] = text[y][:x] + text[y][x + 1:]
                elif y < len(text) - 1:
                    text[y] += text[y + 1]
                    text.pop(y + 1)
            case "k":
                if x < len(text[y]):
                    buff = text[y][x:]
                    text[y] = text[y][:x]
                elif y < len(text) - 1:
                    text[y] += text[y + 1]
                    text.pop(y + 1)
                    buff = "\n"
            case "y":
                if buff == "\n":
                    text.insert(y + 1, text[y][x:])
                    text[y] = text[y][:x]
                    x = 0
                    y += 1
                elif buff:
                    text[y] = text[y][:x] + buff + text[y][x:]
                    x += len(buff)
            case _:  # ignore invalid commands
                continue

    print(*text, sep="\n")

process()