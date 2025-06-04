while True:
    S = input()
    if S == "#":
        break
    status = "A"
    i = 0
    while i < len(S):
        c = S[i]
        if status == "A":
            if c == "0":
                status = "X"
            else:
                status = "Y"
        else:
            if status == "B":
                if c == "0":
                    status = "Y"
                else:
                    status = "X"
            else:
                if status == "X":
                    if c == "0":
                        status = "NA"
                    else:
                        status = "Z"
                else:
                    if status == "Y":
                        if c == "0":
                            status = "X"
                        else:
                            status = "NA"
                    else:
                        if status == "Z":
                            if c == "0":
                                status = "W"
                            else:
                                status = "B"
                        else:
                            if status == "W":
                                if c == "0":
                                    status = "B"
                                else:
                                    status = "Y"
                            else:
                                status = "NA"
        i += 1
    if status == "B":
        print("Yes")
    else:
        print("No")