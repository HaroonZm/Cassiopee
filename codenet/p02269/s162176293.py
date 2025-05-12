def main():
    dictionary = {}
    input_num = int(raw_input())
    counter = 0
    while counter < input_num:
        command, key = raw_input().split(' ')
        if command[0] == 'i':
            dictionary[key] = True
        else:
            if key in dictionary:
                print 'yes'
            else:
              print 'no'

        counter += 1

if __name__ == '__main__':
    main()