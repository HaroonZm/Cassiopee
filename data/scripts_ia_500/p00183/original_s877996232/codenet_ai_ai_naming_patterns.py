while True:
    input_string = raw_input()
    if input_string == "0":
        break
    input_string += "".join([raw_input() for index in range(2)])
    winning_combinations = [(index, index + 1, index + 2) for index in range(0, 9, 3)] + [(index, index + 3, index + 6) for index in range(3)] + [(0, 4, 8), (2, 4, 6)]
    for first, second, third in winning_combinations:
        if input_string[first] == input_string[second] == input_string[third] != "+":
            print "b" if input_string[first] == "b" else "w"
            break
    else:
        print "NA"