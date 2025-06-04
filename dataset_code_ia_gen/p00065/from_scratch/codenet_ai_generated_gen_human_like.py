import sys

def parse_data(lines):
    data = {}
    for line in lines:
        if line.strip() == '':
            continue
        c, d = line.strip().split(',')
        c = int(c)
        # 日付は使わないので無視してもよいが保持してもよい
        data[c] = data.get(c, 0) + 1
    return data

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]
    # 空行で分割
    try:
        blank_index = lines.index('')
    except ValueError:
        blank_index = len(lines)
    last_month_lines = lines[:blank_index]
    this_month_lines = lines[blank_index+1:]
    last_month = parse_data(last_month_lines)
    this_month = parse_data(this_month_lines)
    # 2ヶ月連続で取引がある会社を抽出し、取引回数合計で出力
    common_clients = set(last_month.keys()) & set(this_month.keys())
    for c in sorted(common_clients):
        count = last_month[c] + this_month[c]
        print(c, count)

if __name__ == '__main__':
    main()