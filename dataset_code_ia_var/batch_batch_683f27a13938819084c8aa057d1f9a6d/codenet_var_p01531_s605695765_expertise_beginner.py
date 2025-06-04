flicks = {}
flicks["T"] = "a"
flicks["L"] = "i"
flicks["U"] = "u"
flicks["R"] = "e"
flicks["D"] = "o"

buttons = {}
buttons["1"] = ""
buttons["2"] = "k"
buttons["3"] = "s"
buttons["4"] = "t"
buttons["5"] = "n"
buttons["6"] = "h"
buttons["7"] = "m"
buttons["8"] = "y"
buttons["9"] = "r"
buttons["0"] = "w"

def get_word(button, flick):
    if button == "0" and flick == "U":
        return "nn"
    else:
        return buttons[button] + flicks[flick]

cmds = input()

result = ""
i = 0
while i < len(cmds):
    button = cmds[i]
    flick = cmds[i+1]
    word = get_word(button, flick)
    result = result + word
    i = i + 2

print(result)