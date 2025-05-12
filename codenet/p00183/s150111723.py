while True:

    input_data1 = input()

    if input_data1 == "0":
        break

    input_data2 = input()
    input_data3 = input()

    output = "NA"

    if input_data1[0] != "+" and input_data1[0] == input_data1[1] == input_data1[2]:
        output = input_data1[0]
    elif input_data2[0] != "+" and input_data2[0] == input_data2[1] == input_data2[2]:
        output = input_data2[0]
    elif input_data3[0] != "+" and input_data3[0] == input_data3[1] == input_data3[2]:
        output = input_data3[0]

    elif input_data1[0] != "+" and input_data1[0] == input_data2[0] == input_data3[0]:
        output = input_data1[0]
    elif input_data1[1] != "+" and input_data1[1] == input_data2[1] == input_data3[1]:
        output = input_data1[1]
    elif input_data1[2] != "+" and input_data1[2] == input_data2[2] == input_data3[2]:
        output = input_data1[2]

    elif input_data1[0] != "+" and input_data1[0] == input_data2[1] == input_data3[2]:
        output = input_data1[0]
    elif input_data1[2] != "+" and input_data1[2] == input_data2[1] == input_data3[0]:
        output = input_data1[2]

    print(output)