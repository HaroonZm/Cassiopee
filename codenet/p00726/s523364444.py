def uncompress(text, L):
    newText = ''
    pos = 0
    while True:
        if len(newText) > L:
            break
        if pos >= len(text):
            break
        if text[pos].isdigit():
            endDigit = getEndDigit(text, pos)
            num = int(text[pos : endDigit])
            if text[endDigit] == '(':
                endPar = getEndParenthesis(text, endDigit)
                insideText = uncompress(text[endDigit + 1 : endPar - 1], L - len(newText))
                for _ in range(num):
                    newText += insideText
                    if len(newText) > L:
                        break
                pos = endPar
            else:
                newText += (text[endDigit] * num)
                pos = endDigit + 1
        else:
            newText += text[pos]
            pos += 1
    return newText

def getEndParenthesis(text, pos):
    count = 0
    while True:
        if text[pos] == '(':
            count += 1
        elif text[pos] == ')':
            count -= 1
        if count == 0:
            return pos + 1
        pos += 1

def getEndDigit(text, pos):
    while True:
        if not text[pos].isdigit():
            return pos
        pos += 1

if __name__ == '__main__':
    while True:
        text, idx = input().strip().split()
        if text == '0' and idx == '0':
            break

        text = uncompress(text, int(idx))
        print(text[int(idx)] if len(text) > int(idx) else 0)