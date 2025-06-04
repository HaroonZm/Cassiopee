while True:
    x = raw_input()
    i = x.index(" ")
    if x[i+1] == "?":
        break
    print eval(x)