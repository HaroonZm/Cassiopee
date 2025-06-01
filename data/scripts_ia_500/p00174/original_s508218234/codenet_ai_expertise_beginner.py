while True:
    input_item = input()

    if input_item == "0":
        break

    input_list = []
    input_list.append(input_item)
    input_list.append(input())
    input_list.append(input())

    for item in input_list:
        a_count = item.count("A")
        b_count = item.count("B")

        # enlever le premier caractere
        if item[0] == "A":
            a_count -= 1
        elif item[0] == "B":
            b_count -= 1

        if a_count > b_count:
            a_count += 1
        else:
            b_count += 1

        print(a_count, b_count)