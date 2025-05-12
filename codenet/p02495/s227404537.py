while(True):
    H, W = map(int, raw_input().split())
    if(H == 0 and W == 0):
        break
    s = ["", ""]
    temp = "#.#"
    for i in range(W):
        s[0] += temp[i % 2]
        s[1] += temp[i % 2 + 1]
    for i in range(H):
        print(s[i % 2])
    print("")