n = int(input())
user = []
for i in range(n):
    user.append(input())

m = int(input())
locked = True
for i in range(m):
    t = input()
    found = False
    for u in user:
        if t == u:
            found = True
            break
    if found:
        if locked:
            locked = False
            print("Opened by", t)
        else:
            locked = True
            print("Closed by", t)
    else:
        print("Unknown", t)