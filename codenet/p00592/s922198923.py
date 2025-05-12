#入力数値を分単位に変更
def convert_time(n):
    return (n/100)*60 + n%100

#コマーシャルの共通部分を返す
def kyotsu(cm1,cm2):
    result = []
    for i in range(len(cm2)/2):
        #cm2の各CMとかぶっている部分を取得
        for j in range(len(cm1)/2):
            stt = max(cm2[i*2],cm1[j*2])
            edt = min(cm2[i*2+1],cm1[j*2+1])
            if edt - stt > 0:
                result.append(stt)
                result.append(edt)

    return result

#コマーシャルを見ずにテレビを見られる最長時間を求める
while 1:
    cond = [int(r) for r in raw_input().split()]
    if cond[0]==cond[1]==cond[2]==0: #入力がすべて0なら終了
        break

    #開始時間、終了時間を算出
    start = convert_time(cond[1])
    end = convert_time(cond[2])

    cms = []
    #各チャンネルのコマーシャル時間を求める
    for i in range(cond[0]):
        n = int(raw_input()) #コマーシャル数
        input = [convert_time(int(r)) for r in raw_input().split()]
        j=0
        cmstmp = []
        while j < n:
            st = input[2*j]
            ed = input[2*j+1]
            if not i:
                cms.append(st)
                cms.append(ed)
            else:
                cmstmp.append(st)
                cmstmp.append(ed)
            j += 1
        if i > 0:
            cms = kyotsu(cms,cmstmp)

    #cmsを利用してコマーシャルを見なくてすむ最大時間を出力
    cms = [start] + cms + [end]
    print max([cms[i*2+1]-cms[i*2] for i in range(len(cms)/2)])