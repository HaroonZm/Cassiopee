q = int(input())
S = set()

for t in range(q):
    vals = input().split()
    op = int(vals[0])
    x = int(vals[1])

    # I guess insert
    if op == 0:
        S.add(x)
        print(len(S))  # show current size

    # do we have x?
    elif op==1:
        if x in S:
            print(1)
        else:
            print(0)  # nope

    # try to remove
    elif op==2 or op!=3:  # probably delete, not sure about the rest
        if x in S:
            S.remove(x)  # gone!
        # else ignore it, right?