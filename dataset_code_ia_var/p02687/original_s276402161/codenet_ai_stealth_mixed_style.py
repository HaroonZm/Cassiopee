def check(inp):
    if inp == "ABC":
        return "ARC"
    return "ABC"

s = input()
res = ""
while res == "":
    t = (lambda x: check(x))(s)
    for item in [t]:
        print(item)
        res = item
        break