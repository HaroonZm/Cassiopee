h_r = input().split()
h = int(h_r[0])
r = int(h_r[1])

if h == -r:
    print(0)
else:
    if h > -r:
        print(1)
    else:
        print(-1)