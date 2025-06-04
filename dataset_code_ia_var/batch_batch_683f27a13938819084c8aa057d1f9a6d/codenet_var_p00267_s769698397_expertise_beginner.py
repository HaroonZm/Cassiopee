while True:
    user_input = input()
    if user_input == '0':
        break

    a_input = input()
    b_input = input()

    a_list = [int(x) for x in a_input.split()]
    b_list = [int(x) for x in b_input.split()]

    a_list.sort()
    a_list = a_list[::-1]

    b_list.sort()
    b_list = b_list[::-1]

    p = 0
    c = 0
    found = False

    for i in range(len(a_list)):
        x = a_list[i]
        if i / 2 < c:
            print(i)
            found = True
            break
        if x <= b_list[p]:
            p = p + 1
        else:
            c = c + 1
    if not found:
        print('NA')