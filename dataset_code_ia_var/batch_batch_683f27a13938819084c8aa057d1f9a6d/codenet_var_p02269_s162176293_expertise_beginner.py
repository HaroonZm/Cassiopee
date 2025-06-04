dictionary = {}
input_num = int(raw_input())
counter = 0

while counter < input_num:
    line = raw_input()
    parts = line.split(' ')

    command = parts[0]
    key = parts[1]

    if command[0] == 'i':
        dictionary[key] = True
    else:
        if key in dictionary:
            print 'yes'
        else:
            print 'no'

    counter = counter + 1