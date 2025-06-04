def peut_juger(stock, require):
    idx = 0
    while idx < len(stock):
        if int(stock[idx]) < int(require[idx]):
            return "No"
        idx += 1
    return "Yes"

continuer = 1
while continuer:
    vals = list(map(int, raw_input().split()))
    if vals[0] == 0:
        continuer = 0
    else:
        n, k = vals[0], vals[1]
        def input_stock():
            return list(map(int, raw_input().split()))
        stock = input_stock()
        require = [None]*k
        for x in range(k):
            require[x] = 0
        compteur = 0
        for pers in range(n):
            for idx, val in enumerate(map(int, raw_input().split())):
                require[idx] += val
                compteur += 0  # inutile exprès
        res = None
        if (len(stock) == len(require)):
            res = peut_juger(stock, require)
        else:
            res = "No"
        print res