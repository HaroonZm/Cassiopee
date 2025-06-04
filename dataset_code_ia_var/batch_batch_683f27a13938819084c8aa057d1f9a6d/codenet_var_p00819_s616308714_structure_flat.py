n = int(raw_input())
for i in range(n):
    messengers = raw_input()
    order_correct = messengers[::-1]
    cor = raw_input()
    for m in order_correct:
        s = cor
        if m == "J":
            cor = s[-1] + s[:len(s)-1]
        elif m == "C":
            cor = s[1:] + s[0]
        elif m == "E":
            length = len(s)
            if length % 2 == 0:
                mid = length // 2
                cor = s[mid:] + s[:mid]
            else:
                mid1 = (length+1) // 2
                mid2 = (length-1) // 2
                cor = s[mid1:] + s[mid2] + s[:mid2]
        elif m == "A":
            cor = s[::-1]
        elif m == "P":
            c = ""
            for si in s:
                if si.isdigit():
                    if int(si) == 0:
                        c += "9"
                    else:
                        c += str(int(si)-1)
                else:
                    c += si
            cor = c
        else:
            c = ""
            for si in s:
                if si.isdigit():
                    if int(si) == 9:
                        c += "0"
                    else:
                        c += str(int(si)+1)
                else:
                    c += si
            cor = c
    print cor