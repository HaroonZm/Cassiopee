S = raw_input()
flag = True
if len(S) % 2 == 1:
    flag = False
else:
    for i in range(len(S)/2):
        if S[i] == "b":
            if S[-i-1] != "d":
                flag = False
                break
        elif S[i] == "d":
            if S[-i-1] != "b":
                flag = False
                break
        elif S[i] == "p":
            if S[-i-1] != "q":
                flag = False
                break
        else:
            if S[-i-1] != "p":
                flag = False
                break
       

if flag:
    print "Yes"
else:
    print "No"