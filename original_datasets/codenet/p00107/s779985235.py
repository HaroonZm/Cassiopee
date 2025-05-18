while True:
    d, w, h = map(int, input().split())
    if d == 0:
        break
    d = min(d**2 + w**2, w**2 + h**2, h**2 + d**2)
    n = int(input())
    for i in range(n):
        d_i = (int(input())*2)**2
        if d_i > d:
            print("OK")
        else:
            print("NA")