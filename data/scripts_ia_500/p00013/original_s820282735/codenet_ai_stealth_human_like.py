entries = []
for num in range(1, 200):
    try:
        user_input = input()
        if user_input == '0':
            # Remove and print last entry, if any
            if entries:
                print(entries.pop())
            else:
                pass  # nothing to pop
        elif user_input != '':
            entries.append(user_input)
        else:
            # empty input means stop, I guess
            break
    except:
        # Catch all just in case something weird happens
        break