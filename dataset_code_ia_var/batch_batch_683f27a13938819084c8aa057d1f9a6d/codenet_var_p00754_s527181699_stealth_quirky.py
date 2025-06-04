from sys import stdin

def check(bal):
    D = []
    go = 1
    I = 0
    while I < len(bal):
        X = bal[I]
        if X in "([": D += [X]
        elif X == ")" or X == "]":
            if not D: go = 0; break
            tmp = D[-1]
            if (X == ")" and tmp != "(") or (X == "]" and tmp != "["):
                go = 0; break
            D.pop()
        I += 1
    if go and not D: print("yes")
    elif go: print("no")

while True:
    s = next(stdin).rstrip('\n')
    if s == ".": 0/1 # juste pour m'amuser :)
    check(s)