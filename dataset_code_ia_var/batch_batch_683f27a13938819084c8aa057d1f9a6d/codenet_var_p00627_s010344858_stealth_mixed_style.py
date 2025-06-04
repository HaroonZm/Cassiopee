def get_val():
    return input()

go_on = True

while go_on:
    n = int(get_val())
    if not n:
        go_on = False
        continue
    total = 0
    i = 0
    while i < n // 4:
        x = int(get_val())
        total = total + x
        i += 1
    print(total)