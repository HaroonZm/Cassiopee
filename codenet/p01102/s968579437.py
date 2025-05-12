while True:
    s1 = input()
    if s1 == ".":
        break
    s2 = input()

    w1 = s1.split('"')
    w2 = s2.split('"')

    if len(w1) != len(w2):
        result = "DIFFERENT"
    else:
        n = len(w1)
        result = "IDENTICAL"
        for i in range(n):
            if i % 2 == 0:
                if w1[i] != w2[i]:
                    result = "DIFFERENT"
                    break
            else:
                if w1[i] != w2[i]:
                    if result == "IDENTICAL":
                        result = "CLOSE"
                    else:
                        result = "DIFFERENT"
                        break

    print(result)