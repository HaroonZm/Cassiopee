n = int(input())
user = [input() for i in range(n)]

m = int(input())
locked = True
for i in range(m):
    t = input()
    if t in user:
        if locked:
            locked = False
            print("Opened by", t)
        else:
            locked = True
            print("Closed by", t)
    else:
        print("Unknown", t)