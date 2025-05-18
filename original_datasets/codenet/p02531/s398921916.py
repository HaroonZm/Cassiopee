stuck = ""
while True:
    a = raw_input().split()
    if a[0] == "quit":
        break
    if a[0] == "push":
        stuck += a[1]
    elif a[0] == "pop":
        l = len(stuck) - 1
        print stuck[l]
        stuck = stuck[:l]