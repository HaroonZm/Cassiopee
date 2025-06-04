L = int(input())
cats = list(map(int, input().split()))

hole = []
for i in range(L):
    c = cats[i]
    if c > 0:
        # Cat enters
        if c in hole:
            # Cat already inside, error
            print(i + 1)
            break
        else:
            hole.append(c)
    else:
        # Cat exits
        c_abs = -c
        if len(hole) == 0:
            # No cat inside to exit
            print(i + 1)
            break
        if hole[-1] != c_abs:
            # Cat trying to leave is not last one entered
            print(i + 1)
            break
        else:
            hole.pop()
else:
    # If no error found
    print("OK")