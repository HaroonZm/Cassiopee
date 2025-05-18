while 1:
    n = int(input())
    if n == 0:
        break

    step = list(input().split())
    pos = 0     # 0:bottom, 1:top
    lu, ru, ld, rd = [0] * 4
    cnt = 0

    for s in step:
        if pos == 0:
            if s == "lu":
                lu = 1
            elif s == "ru":
                ru = 1
            elif s == "ld":
                lu = 0
            elif s == "rd":
                ru = 0

            if lu == 1 and ru == 1:
                cnt += 1
                pos = 1
                lu, ru = 0, 0

        elif pos == 1:
            if s == "ld":
                ld = 1
            elif s == "rd":
                rd = 1
            elif s == "lu":
                ld = 0
            elif s == "ru":
                rd = 0

            if ld == 1 and rd == 1:
                cnt += 1
                pos = 0
                ld, rd = 0, 0

    print(cnt)