n = int(input())
for _ in range(n):
    s = input()
    tokens = []
    i = 0
    # 分割しておく
    while i < len(s):
        if s[i].isalpha():
            tokens.append(s[i])
            i += 1
        else:
            if s[i:i+2] == '->':
                tokens.append('->')
                i += 2
            elif s[i:i+2] == '<-':
                tokens.append('<-')
                i += 2
            else:
                i += 1

    # 車両の列をリストで表現する。先頭は0番目
    train = [tokens[0]]
    # 今現在の車両のindex
    pos = 0

    # tokensの1つ目は車両文字、2つ目以降は操作と車両文字の繰り返し
    # 2つずつ見ていく
    for i in range(1, len(tokens), 2):
        op = tokens[i]  # -> または <-
        car = tokens[i+1]  # 次の車両文字

        if op == '->':
            # 後方へ移動。現在の車両の後ろをチェック
            if pos == len(train) - 1:
                # 末尾なら追加
                train.append(car)
                pos += 1
            else:
                # 次の車両がcarになるはず
                if train[pos+1] != car:
                    # 違うならそこにcarを挿入
                    train.insert(pos+1, car)
                pos += 1
        else:
            # 前方へ移動。現在の車両の前をチェック
            if pos == 0:
                # 先頭なら挿頭
                train.insert(0, car)
                # posは一つ後ろにずれる
                pos = 0
            else:
                if train[pos-1] != car:
                    train.insert(pos, car)
                pos -= 1

    print(''.join(train))