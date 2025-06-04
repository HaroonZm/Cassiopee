while True:
    try:
        n = int(input())
        S = (n - 1) % 39 + 1
        S_str = str(S)
        if S < 10:
            S_str = "0" + S_str
        print("3C" + S_str)
    except:
        break