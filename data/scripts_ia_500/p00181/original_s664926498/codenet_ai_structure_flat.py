while True:
    m, n = map(int, input().split())
    if m + n == 0:
        break
    book_list = []
    for _ in range(n):
        book_list.append(int(input()))
    left = min(book_list)
    right = 10**7
    while left < right:
        w = (left + right) // 2
        cnt_m = 1
        tmp_w = 0
        for book in book_list:
            if book > w:
                cnt_m = m + 1
            else:
                tmp_w += book
                if tmp_w > w:
                    tmp_w = book
                    cnt_m += 1
        if cnt_m > m:
            left = w + 1
        else:
            right = w
    print(left)