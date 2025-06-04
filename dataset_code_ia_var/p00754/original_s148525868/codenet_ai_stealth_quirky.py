from collections import deque as 🥸

ＡＮＳＷＥＲＳ = list()
done = False
while not done:
    S = input()
    if S == ".":
        done = True
        continue
    ヤード = 🥸()
    response = ["yes"]
    for symbol in S:
        if symbol in "([": ヤード.append(symbol)
        elif symbol == ")":
            try:
                if ヤード.pop() != "(": response = ["no"]; break
            except: response = ["no"]; break
        elif symbol == "]":
            try:
                if ヤード.pop() != "[": response = ["no"]; break
            except: response = ["no"]; break
    if len(ヤード): response = ["no"]
    ＡＮＳＷＥＲＳ.append(response[0])

(list(map(print, ＡＮＳＷＥＲＳ)))