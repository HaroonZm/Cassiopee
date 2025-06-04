while True:
    s = input()
    if s == "END OF INPUT":
        break
    parts = s.split(' ')
    res = [str(len(x)) for x in parts]
    print(''.join(res))