n = int(raw_input())
loop = 0
while loop < n:
    manu = raw_input()
    msg = raw_input()
    size = len(msg)
    i = len(manu) - 1
    while i >= 0:
        s = manu[i]
        if s == "J":
            if size > 1:
                msg = msg[-1] + msg[:-1]
        elif s == "C":
            if size > 1:
                msg = msg[1:] + msg[0]
        elif s == "E":
            if size == 1:
                i -= 1
                continue
            if size % 2 == 0:
                msg = msg[size // 2:] + msg[:size // 2]
            else:
                msg = msg[size // 2 + 1:] + msg[size // 2] + msg[:size // 2]
        elif s == "A":
            msg = msg[::-1]
        elif s == "P":
            j = 0
            while j < len(msg):
                if msg[j].isdigit():
                    msg = msg[:j] + str((int(msg[j]) - 1 + 10) % 10) + msg[j + 1:]
                j += 1
        elif s == "M":
            j = 0
            while j < len(msg):
                if msg[j].isdigit():
                    msg = msg[:j] + str((int(msg[j]) + 1) % 10) + msg[j + 1:]
                j += 1
        i -= 1
    print msg
    loop += 1