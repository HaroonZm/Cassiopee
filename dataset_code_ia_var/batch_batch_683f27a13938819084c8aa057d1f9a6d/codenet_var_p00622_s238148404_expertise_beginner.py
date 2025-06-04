while True:
    s1 = input()
    if s1 == "-":
        break
    s2 = input()
    under = input()

    s1_list = list(s1)
    s2_list = list(s2)
    under_list = list(under)

    s1_list.reverse()
    s2_list.reverse()
    under_list.reverse()

    right = []
    if len(s2_list) > 0:
        center = s2_list.pop()
    else:
        center = ""

    while len(s1_list) > 0 or len(s2_list) > 0:
        if len(under_list) > 0 and center == under_list[-1]:
            if len(s1_list) > 0:
                center = s1_list.pop()
            else:
                center = ""
            under_list.pop()
        else:
            right.append(center)
            if len(s2_list) > 0:
                center = s2_list.pop()
            else:
                center = ""

    if len(under_list) == 0:
        right.append(center)

    print("".join(right))