while 1:
    a = input()
    if a == "END OF INPUT":
        break
    else:
        c = 0
        for i in a:
            if i == ' ':
                print(c,end = "")
                c = 0
            else:
                c += 1
        print(c)