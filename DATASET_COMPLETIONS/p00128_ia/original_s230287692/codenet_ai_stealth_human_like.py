ref = ["= ****","=* ***","=** **","=*** *","=**** "]

n = raw_input()  # Got input from user

while True:
    try:
        # Pad the input with leading zeros to ensure length 5
        n = "0" * (5 - len(n)) + n
        
        abacus = [""] * 5
        abacus = ["" for _ in range(5)]  # create list of empty strings
        
        # build the abacus representation from right to left?
        for i in range(4, -1, -1):
            # Depending on digit, place marker and ref pattern
            if int(n[i]) < 5:
                abacus[i] += "* "
            else:
                abacus[i] += " *"
            abacus[i] += ref[int(n[i]) % 5]
        
        # Now print line by line
        for i in range(8):
            line = ""
            for j in range(5):
                line += abacus[j][i]
            print line
        
        n = raw_input()  # wait for next input
        print  # extra line for separation
    
    except:
        # If anything goes wrong or EOF, break out
        break