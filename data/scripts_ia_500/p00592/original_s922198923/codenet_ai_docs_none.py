def convert_time(n):
    return (n/100)*60 + n%100

def kyotsu(cm1,cm2):
    result = []
    for i in range(len(cm2)//2):
        for j in range(len(cm1)//2):
            stt = max(cm2[i*2],cm1[j*2])
            edt = min(cm2[i*2+1],cm1[j*2+1])
            if edt - stt > 0:
                result.append(stt)
                result.append(edt)
    return result

while True:
    cond = [int(r) for r in raw_input().split()]
    if cond[0]==0 and cond[1]==0 and cond[2]==0:
        break

    start = convert_time(cond[1])
    end = convert_time(cond[2])

    cms = []
    for i in range(cond[0]):
        n = int(raw_input())
        input = [convert_time(int(r)) for r in raw_input().split()]
        j=0
        cmstmp = []
        while j < n:
            st = input[2*j]
            ed = input[2*j+1]
            if i == 0:
                cms.append(st)
                cms.append(ed)
            else:
                cmstmp.append(st)
                cmstmp.append(ed)
            j += 1
        if i > 0:
            cms = kyotsu(cms,cmstmp)

    cms = [start] + cms + [end]
    print max([cms[i*2+1]-cms[i*2] for i in range(len(cms)//2)])