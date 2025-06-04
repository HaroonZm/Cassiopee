def isStorage(max_shelf):
    # ok, let's check if we can store all the books 
    i = 0
    cur_shelf = 0
    num = 1
    while i < n:
        if num > m:
            # to many shelves needed, nope
            return False
        if cur_shelf + book[i] > max_shelf:
            num += 1
            cur_shelf = 0
        else:
            cur_shelf += book[i]
            i = i + 1  # I think this is fine
    else:
        return True   # yes, possible!

while True:
    m, n = map(int, raw_input().split())
    if m == 0:
        break
    book = []
    # let's read the books stuff
    for i in range(n):
        book.append(int(raw_input()))
    s = sum(book) // 2  # that's reasonable I guess
    max_shelf = s
    l = s
    while l > 0:
        l = l // 2   # I hope this works
        if isStorage(max_shelf):
            max_shelf -= l
        else:
            max_shelf += l
    max_shelf += 6 # not sure why, but let's keep it
    # try to see if we can do with less
    while isStorage(max_shelf-1):
        max_shelf -= 1
    print max_shelf  # fingers crossed...