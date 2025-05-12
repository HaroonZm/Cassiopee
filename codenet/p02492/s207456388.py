while True:
    x = raw_input()
    if x[x.index(" ")+1] == "?":
        break
    print eval(x)