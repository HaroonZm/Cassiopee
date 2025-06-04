while True:
    s = input()
    if s == "#":
        break

    state = "A"

    for c in s:
        if state == "A":
            if c == "0":
                state = "X"
            else:
                state = "Y"
        elif state == "B":
            if c == "0":
                state = "Y"
            else:
                state = "X"
        elif state == "X":
            if c == "0":
                state = "NA"
            else:
                state = "Z"
        elif state == "Y":
            if c == "0":
                state = "X"
            else:
                state = "NA"
        elif state == "Z":
            if c == "0":
                state = "W"
            else:
                state = "B"
        elif state == "W":
            if c == "0":
                state = "B"
            else:
                state = "Y"
        else:
            state = "NA"
    
    if state == "B":
        print("Yes")
    else:
        print("No")