for loop in range(int(raw_input())):
    manu = raw_input()
    msg = raw_input()
    size = len(msg)
    
    for s in manu[::-1]:
        if   s == "J":
            msg = msg[-1]+msg[:-1] if size > 1 else msg
        elif s == "C":
            msg = msg[1:]+msg[0] if size > 1 else msg
        elif s == "E":
            if size == 1: continue
            if size%2 == 0:
                msg = msg[size/2:]+msg[:size/2]
            else:
                msg = msg[size/2+1:]+msg[size/2]+msg[:size/2]
        elif s == "A":
            msg = msg[::-1]
        elif s == "P":
            for i in range(len(msg)):
                if msg[i].isdigit():
                    msg = msg[:i]+str((int(msg[i])-1+10)%10)+msg[i+1:]
        elif s == "M":
            for i in range(len(msg)):
                if msg[i].isdigit():
                    msg = msg[:i]+str((int(msg[i])+1)%10)+msg[i+1:]
    
    print msg