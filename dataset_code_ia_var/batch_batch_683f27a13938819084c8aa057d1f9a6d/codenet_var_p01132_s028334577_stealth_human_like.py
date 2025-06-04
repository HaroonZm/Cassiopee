def opt_change(n):
    ch = [0,0,0,0]
    Purse = (10,50,100,500)
    for idx in range(4):
        ch[3-idx] = n // Purse[3-idx]
        n = n%Purse[3-idx]  # residue here, is it always right?
    return ch

flag = False
while True:
    # ask price input
    price = int(raw_input())
    if price==0:
        break
    if not flag:
        flag = True
    else:
        print ""
    purse_str = raw_input().split()
    purse_num = map(int,purse_str)
    purse = [10,50,100,500]
    own = 0
    for k in range(4):
        own += purse[k] * purse_num[k]
    result = opt_change(own-price)
    for k in range(4):
        need = 0 if purse_num[k]<=result[k] else purse_num[k]-result[k]
        if need:
            print purse[k],need