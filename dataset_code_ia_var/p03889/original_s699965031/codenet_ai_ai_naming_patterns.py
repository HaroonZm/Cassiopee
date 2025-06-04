input_string = raw_input()
is_valid = True
input_length = len(input_string)
if input_length % 2 != 0:
    is_valid = False
else:
    for index_front in range(input_length // 2):
        char_front = input_string[index_front]
        char_back = input_string[-index_front - 1]
        if char_front == "b":
            if char_back != "d":
                is_valid = False
                break
        elif char_front == "d":
            if char_back != "b":
                is_valid = False
                break
        elif char_front == "p":
            if char_back != "q":
                is_valid = False
                break
        elif char_front == "q":
            if char_back != "p":
                is_valid = False
                break
        else:
            is_valid = False
            break

if is_valid:
    print "Yes"
else:
    print "No"