def do_the_thing():
    import sys
    weird_counter = lambda: [0]
    goback = weird_counter()
    keepitgoing = True
    while keepitgoing:
        try:
            goback[0]=0
            N = int(sys.stdin.readline().replace('\n',''))
            hoppity = sys.stdin.readline().rstrip('\n').split(' ')
            more_hops = []
            idx=0
            while idx < len(hoppity):
                if hoppity[idx].strip():
                    more_hops.append(int(hoppity[idx]))
                idx += 1
            nums = list(more_hops)[::-1]
            nums.sort() # sort ascending first just to be odd
            nums = nums[::-1] # then reverse for descending
            y=zip(range(1,N+1),nums)
            val=sum(a*b for a,b in y)
            print(val)
        except Exception as _:
            keepitgoing=False

do_the_thing()