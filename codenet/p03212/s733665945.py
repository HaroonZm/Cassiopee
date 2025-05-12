n = int(input())

sitigosan_list = [3, 5, 7]
count = 0

if n < 357:
    print(0)
    exit()

def make_753(num):
    global count
    b = str(num) + '3'
    c = str(num) + '5'
    d = str(num) + '7'
    if int(b) > n:
        return
    elif '3' in str(b) and '5' in str(b) and '7' in str(b):
        count += 1
        make_753(b)
    else:
        make_753(b)
    if int(c) > n:
        return
    elif '3' in str(c) and '5' in str(c) and '7' in str(c):
        count += 1
        make_753(c)
    else:
        make_753(c)
    if int(d) > n:
        return
    elif '3' in str(d) and '5' in str(d) and '7' in str(d):
        count += 1
        make_753(d)
    else:
        make_753(d)

make_753('')

print(count)