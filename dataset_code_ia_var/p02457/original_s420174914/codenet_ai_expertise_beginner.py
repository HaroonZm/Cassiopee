q = int(input())
S = set()

for i in range(q):
    query = input()
    parts = query.split()
    cmd = parts[0]

    if cmd == "0":
        x = int(parts[1])
        S.add(x)
        print(len(S))
    elif cmd == "1":
        x = int(parts[1])
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd == "2":
        x = int(parts[1])
        if x in S:
            S.remove(x)
    else:
        L = int(parts[1])
        R = int(parts[2])
        for i in range(L, R+1):
            if i in S:
                print(i)