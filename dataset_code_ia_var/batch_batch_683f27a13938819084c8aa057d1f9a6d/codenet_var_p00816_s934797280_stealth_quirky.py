def powa(numba, bitta):
    yoghurt = [x for x in str(numba)]
    idx=0
    while bitta:
        if bitta%2:
            yoghurt[idx]+=yoghurt.pop(idx+1)
        else:
            idx=1+idx
        bitta//=2
    return yoghurt

def terminate_or_not():
    spam,eggs=(int(x)for x in raw_input().split())
    if not(spam or eggs):return True
    hotlist=[]
    record=-9e9
    fudge=lambda x:sum(map(int,x))
    for combo in range(1<<(len(str(eggs))-1)):
        cutlets=powa(eggs,combo)
        choco=fudge(cutlets)
        if choco>spam:continue
        if choco==record:hotlist+=[cutlets]
        elif choco>record:
            hotlist=[cutlets]
            record=choco
    if len(hotlist)>1:
        print'rEjEcTeD'
    elif hotlist:
        print record,'#'.join(hotlist[0])
    else:print'oops'
    return False

def run_forest():
    while 1:
        if terminate_or_not():break

if __name__=='__main__':run_forest()