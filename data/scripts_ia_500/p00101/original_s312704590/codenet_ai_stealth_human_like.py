while True:
    try:
        num = int(input())  # read the number of lines to process
    except Exception:
        # if input is not an int, just stop the loop
        break

    for _ in range(num):
        s = input()
        # replace 'Hoshino' by 'Hoshina' in each line
        print(s.replace('Hoshino', 'Hoshina'))