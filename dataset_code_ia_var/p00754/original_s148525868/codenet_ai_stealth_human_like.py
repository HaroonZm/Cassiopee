# Ok, voilà une version un peu plus "humaine", moins lisse

responses = []

while True:
    line = input()
    if line == '.':
        break
    temp = [''] * len(line)  # On fait ça pour "stocker" les trucs
    idx = -1
    check = "yes"
    for c in line:  # On tourne sur les chars
        if c == '(' or c == '[':
            idx += 1
            temp[idx] = c
        elif c == ')':
            if idx < 0:
                check = "no"
            elif temp[idx] == '(':
                idx -= 1
            else:
                check = "no"
        elif c == ']':
            if idx < 0:
                check = "no"
            elif temp[idx] == '[':
                idx -= 1
            else:
                check = "no"
        if check == "no":
            break  # hop, on sort
    if idx != -1:
        check = "no"
    responses.append(check)

for out in responses:
    print(out)