S = input()

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
else:

    code = list(map(lambda x : ord(x) - ord('a'), list(S)))

    done = False
    for i in range(26):
        if not i in code:
            code.append(i)
            done = True
            break

    while len(code) > 0 and not done:
        last = code[-1]
        code = code[:-1]
        if last == 25:
            continue
        else:
            for i in range(last+1, 26):
                if i not in code:
                    code.append(i)
                    done = True
                    break

    decode = list(map(lambda x : chr(x + ord('a')), code))
    print(''.join(decode))