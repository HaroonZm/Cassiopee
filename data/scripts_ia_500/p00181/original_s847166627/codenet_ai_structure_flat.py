while 1:
    m, n = map(int, raw_input().split())
    if m == 0: 
        break
    book = [int(raw_input()) for i in range(n)]
    max_shelf = sum(book) / 2
    length = max_shelf
    def isStorage(max_shelf):
        i = 0
        cur_shelf = 0
        num = 1
        while i < n:
            if num > m:
                return False
            if cur_shelf + book[i] > max_shelf:
                num += 1
                cur_shelf = 0
            else:
                cur_shelf += book[i]
                i += 1
        return True
    while length:
        length /= 2
        if isStorage(max_shelf):
            max_shelf -= length
        else:
            max_shelf += length
    max_shelf += 6
    while isStorage(max_shelf - 1):
        max_shelf -= 1
    print max_shelf