import sys

if sys.version[0] == '2':
    range = xrange
    input = raw_input

while True:
    line = input().split()
    W = int(line[0])
    D = int(line[1])
    if W == 0 and D == 0:
        break
    hw_list = input().split()
    hw = []
    for x in hw_list:
        hw.append(int(x))
    hd_list = input().split()
    hd = []
    for x in hd_list:
        hd.append(int(x))

    common = []
    for h in hw:
        if h in hd:
            common.append(h)
            hd.remove(h)

    result = sum(hw) + sum(hd) - sum(common)
    print(result)