while True:
    try:
        s = input()
        JOI = 0
        IOI = 0
        for i in range(len(s) - 2):
            if s[i] == 'J' and s[i+1] == 'O' and s[i+2] == 'I':
                JOI = JOI + 1
            elif s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
                IOI = IOI + 1
        print(JOI)
        print(IOI)
    except:
        break