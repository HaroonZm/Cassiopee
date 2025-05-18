while True:
    try:
        n=int(input())
        S=(n-1)%39+1
        print("3C",format(S,"02d"),sep="")
    except:
        break