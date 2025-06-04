flicks = dict(T="a", L="i", U="u", R="e", D="o")

def get_but(b):
    return {
        "1": "",
        "2": "k",
        "3": "s",
        "4": "t",
        "5": "n",
        "6": "h",
        "7": "m",
        "8": "y",
        "9": "r",
        "0": "w"
    }[b]

def synth(b, f):
    if b == "0":
        if f == "U":
            return "nn"
    return get_but(b) + flicks.get(f)

cmds = input()
out = []
i = 0
while i < len(cmds):
    out.append(synth(cmds[i],cmds[i+1]))
    i += 2
print("".join(out))