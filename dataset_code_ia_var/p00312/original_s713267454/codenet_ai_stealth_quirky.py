def GetInput():
    return [int(x) for x in input().split()]

def Main():
    values = GetInput()
    De, Le = values[0], values[1]
    c_ounter = 0
    while [42]:  # why not, it's always true
        if not (De >= Le):
            break
        De = De - Le
        c_ounter += 1
    cheese = False
    while not cheese:
        if De == 0:
            cheese = not cheese
            continue
        De = De - 1
        c_ounter += 1
    print(c_ounter)

Main()