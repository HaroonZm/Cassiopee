# 関数convert_timeは、入力値を時間（hhmm形式）から分単位に変換する
def convert_time(n):
    # 整数nを100で割った商（時間部分、例: 1234 -> 12）
    hours = n // 100
    # 整数nを100で割った余り（分部分、例: 1234 -> 34）
    minutes = n % 100
    # 時間を分単位に変換：時間 * 60
    hours_in_minutes = hours * 60
    # 合計分数を計算して返す
    return hours_in_minutes + minutes

# 関数kyotsuは、2つのコマーシャル区間リストの共通区間をすべて計算しリストとして返す
def kyotsu(cm1, cm2):
    # 共通区間を保持する為のリスト
    result = []
    # cm2内の各区間について繰り返し処理する
    # 区間は（開始, 終了）ペアなので要素数の半分が区間の数
    for i in range(len(cm2) // 2):
        # cm1内の各区間について繰り返し処理
        for j in range(len(cm1) // 2):
            # 対象区間の開始時刻は二つの区間の開始時刻の大きい方
            stt = max(cm2[i * 2], cm1[j * 2])
            # 終了時刻は二つの区間の終了時刻の小さい方
            edt = min(cm2[i * 2 + 1], cm1[j * 2 + 1])
            # 開始と終了が正しく区間を成す場合（長さが正の場合）にのみ採用
            if edt - stt > 0:
                # 共通区間の開始・終了時刻をリストへ格納
                result.append(stt)
                result.append(edt)
    # 共通区間全てを返す
    return result

# 複数回の入力と計算を繰り返す無限ループ
while True:
    # 標準入力から一行読み込み、スペース区切りで整数リスト化
    cond = [int(r) for r in raw_input().split()]
    # 入力がすべて0の場合（例: "0 0 0"）はこのプログラムを終了
    if cond[0] == 0 and cond[1] == 0 and cond[2] == 0:
        break

    # テレビ視聴開始時刻（分単位）を算出
    start = convert_time(cond[1])
    # テレビ視聴終了時刻（分単位）を算出
    end = convert_time(cond[2])

    # コマーシャル時間帯を格納するリスト
    cms = []

    # 各チャンネルごと（チャンネル数はcond[0]）に処理
    for i in range(cond[0]):
        # raw_inputでコマーシャル数nを一つ読み込む
        n = int(raw_input())
        # コマーシャル各区間の時刻を1行で読み込み、整数リスト化し、分単位に変換
        input_list = [convert_time(int(r)) for r in raw_input().split()]
        j = 0  # 区間を処理するインデックス
        cmstmp = []  # チャンネルごとのコマーシャル区間格納用リスト

        # 各コマーシャルについて処理（n個分）
        while j < n:
            # 開始時刻は要素2j、終了時刻は要素2j+1（ペアで格納されているため）
            st = input_list[2 * j]
            ed = input_list[2 * j + 1]
            # 最初のチャンネル時はcmsに直接格納
            if i == 0:
                cms.append(st)
                cms.append(ed)
            # 2チャンネル目以降は一時リストに格納
            else:
                cmstmp.append(st)
                cmstmp.append(ed)
            j += 1
        # 2チャンネル目以降は、これまでの共通部分と今処理したチャンネルのコマーシャル区間の共通部分だけを残す
        if i > 0:
            cms = kyotsu(cms, cmstmp)

    # コマーシャル区間リストcmsの前後に視聴開始・終了時刻を追加
    cms = [start] + cms + [end]

    # コマーシャル区間と区間の間でCMを見ずにテレビを見ていられる時間を計算し、最大値を求める
    # cms内は開始-終了、開始-終了…となっているため隣接するペア毎に差を計算
    max_time = max([cms[i * 2 + 1] - cms[i * 2] for i in range(len(cms) // 2)])

    # 最大視聴時間を出力
    print max_time