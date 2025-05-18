# 解答
def abc173_a(lines):
    N = int(lines[0])
    values = map(int, lines[1].split(' '))
    answer = 0
    tmp = list()
    for value in values:
        tmp.append(value)
    for i in range(N):
        if i % 2 != 0:
            pass
        else:
            if tmp[i] % 2 != 0:
                answer += 1
    return [answer]

# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines

# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['5', '1 3 4 5 7']
        lines_export = [2]
    elif pattern == 2:
        lines_input = ['15', '13 76 46 15 50 98 93 77 31 43 84 90 6 24 14']
        lines_export = [3]
    return lines_input, lines_export

# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        mode = 0
    else:
        mode = int(args[1])
    return mode

# 主処理
def main():
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines(2)
    else:
        lines_input, lines_export = get_testdata(mode)

    lines_result = abc173_a(lines_input)

    for line_result in lines_result:
        print(line_result)

    if mode > 0:
        print(f'lines_input=[{lines_input}]')
        print(f'lines_export=[{lines_export}]')
        print(f'lines_result=[{lines_result}]')
        if lines_result == lines_export:
            print('OK')
        else:
            print('NG')

# 起動処理
if __name__ == '__main__':
    main()