while 1:
    s = input()
    n, i, j = map(int, s.split())

    if n==0:
        break

    updown = [None for _ in range(n+1)];

    whole = 2**n
    fold = n
    from_top = i
    while 1:
        if whole == 1:
            assert fold == 0
            break

        half = whole // 2
        if from_top <= half:
            updown[fold] = 0
        else:
            updown[fold] = 1
        
        fold -= 1
        whole = half

        if half >= from_top:
            from_top = half - from_top + 1
        else:
            from_top = from_top - half

    whole = 2**n
    from_left = j
    output = ""
    for i in range(1, n+1):
        half = whole // 2

        if from_left <= half:
            is_right = 0
        else:
            is_right = 1

        if (updown[i] + is_right) % 2 == 0:
            output += "L"
            if half >= from_left:
                from_left = half - from_left + 1
            else:
                from_left = from_left - half
        else:
            output += "R"
            if half < from_left:
                from_left = whole - from_left + 1

        whole = half

    print(output)