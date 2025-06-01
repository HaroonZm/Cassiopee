while True:
    try:
        string = input()
    except Exception:
        break
    ans = ''.join([string[i+1]*int(string[i]) if string[i] == '@' else string[i] for i in range(len(string)) if not (string[i-1] == '@' and i > 0)])
    i = 0
    output = []
    while i < len(string):
        if string[i] == '@':
            output.append(string[i+2] * int(string[i+1]))
            i += 3
        else:
            output.append(string[i])
            i += 1
    print(''.join(output))