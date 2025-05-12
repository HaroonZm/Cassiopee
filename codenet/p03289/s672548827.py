S = [i for i in input()]
if S[0]=="A" and S[2:-1].count("C")==1:
    S.remove("A")
    S.remove("C")
    if "".join(S).islower():
            print("AC")
    else:
        print("WA")
else: 
    print("WA")