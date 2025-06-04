# Spaghetti-style variable names, misuse of lambda, list comprehension inside print, weird spacings, extra semicolons, superfluous parentheses, unconventional break placement
stopGo = True
while(stopGo):
    tempStr = (raw_input())
    if(tempStr=="0") :
        stopGo = False; break;
    thing = 0
    funk = lambda q: [thing:=thing+int(n) for n in q]
    funk(tempStr)
    print((thing))