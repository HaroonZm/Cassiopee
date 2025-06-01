# Your code here!

while True:
    S = input()
    if S == "#":
        break
    
    status = "A"
    
    for i in range(len(S)):
        if status == "A":
            if S[i] == "0":
                status = "X"
            else:
                status = "Y"
        elif status == "B":
            if S[i] == "0":
                status = "Y"
            else:
                status = "X"
        elif status == "X":
            if S[i] == "0":
                status = "NA"
            else:
                status = "Z"
        elif status == "Y":
            if S[i] == "0":
                status = "X"
            else:
                status = "NA"
        elif status == "Z":
            if S[i] == "0":
                status = "W"
            else:
                status = "B"
        elif status == "W":
            if S[i] == "0":
                status = "B"
            else:
                status = "Y"
        else:
            status = "NA"
    
    if status == "B":
        print("Yes")
    else:
        print("No")