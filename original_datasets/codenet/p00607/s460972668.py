text = []
while True:
  s = input()
  if s == "END_OF_TEXT":
    break
  text.append(s)

x, y = 0, 0
buff = ""
while True:
  c = input()
  if c == "-":
    break

  elif c == "a":
    x = 0

  elif c == "e":
    x = len(text[y])

  elif c == "p":
    if y == 0:
      x = 0
    else:
      x = 0
      y -= 1

  elif c == "n":
    if y == len(text) - 1:
      x = 0
    else:
      y += 1
      x = 0

  elif c == "f":
    if x != len(text[y]):
      x += 1
    elif y != len(text) - 1:
      y += 1
      x = 0

  elif c == "b":
    if x != 0:
      x -= 1
    elif y != 0:
      y -= 1
      x = len(text[y])

  elif c =="d":
    if x < len(text[y]):
      text[y] = text[y][:x] + text[y][x + 1:] 
    elif y != len(text) - 1:
      text[y] = text[y] + text[y + 1]
      text = text[:y + 1] + text[y + 2:]

  elif c == "k":
    if x < len(text[y]):
      buff = text[y][x:]
      text[y] = text[y][:x]
    elif y != len(text) - 1:
      text[y] = text[y] + text[y + 1]
      text = text[:y + 1] + text[y + 2:]
      buff = "\n"

  elif c =="y":
    if buff == "\n":
      new_row = text[y][x:]
      text[y] = text[y][:x]
      text = text[:y + 1] + [new_row] + text[y + 1:]
      x = 0
      y += 1
    else:
      text[y] = text[y][:x] + buff + text[y][x:]
      x += len(buff)

print(*text, sep="\n")