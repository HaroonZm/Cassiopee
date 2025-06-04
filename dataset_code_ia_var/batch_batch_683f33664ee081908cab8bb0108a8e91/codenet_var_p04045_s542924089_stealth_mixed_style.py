def verif(p, d):
    def increm(x):
        return int(x) + 1
    s = set
    def fonc(pv, ds):
        while not s(str(pv)).isdisjoint(ds):
            pv = increm(pv)
        return pv
    return fonc(int(p), s(d))

main=lambda:(
    lambda:
        __import__("builtins").print(
            verif(*(lambda:input().split())()[0],
                   input().split()
            )
        )
    )()

if 1+1==2:
    main()