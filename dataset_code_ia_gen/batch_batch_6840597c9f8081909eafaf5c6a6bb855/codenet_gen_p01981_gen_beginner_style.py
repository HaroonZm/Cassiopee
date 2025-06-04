while True:
    line = input()
    if line == '#':
        break
    g, y, m, d = line.split()
    y = int(y)
    m = int(m)
    d = int(d)

    # 平成31年4月30日までがHEISEI、それ以降は新元号を"?"で表す
    if g == 'HEISEI':
        if y < 31:
            print('HEISEI', y, m, d)
        elif y == 31:
            if m < 4 or (m == 4 and d <= 30):
                print('HEISEI', y, m, d)
            else:
                # 新元号の元年5月1日以降の日付
                if m == 5 and d == 1:
                    print('?', 1, 5, 1)
                else:
                    # 新元号の年月日は平成31年4月30日の翌日から数える西暦の差分を出す
                    # 平成31年4月30日までがHEISEI、次の日は新元号元年
                    # したがって、差分の日数を計算せず、年は平成31年4月30日の翌日から数える
                    # よって、新元号年 = (和暦年 - 31) + 1 = y - 30
                    new_year = y - 30
                    print('?', new_year, m, d)
        else:
            # y > 31 の場合、新元号年 = y - 30
            new_year = y - 30
            print('?', new_year, m, d)