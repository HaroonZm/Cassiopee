def abc173_a(lines):
    N = int(lines[0])
    nums = lines[1].split()
    count = 0
    for i in range(N):
        num = int(nums[i])
        if i % 2 == 0:
            if num % 2 == 1:
                count += 1
    return [count]

def get_input_lines(lines_count):
    lines = []
    for _ in range(lines_count):
        lines.append(input())
    return lines

def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['5', '1 3 4 5 7']
        lines_export = [2]
    elif pattern == 2:
        lines_input = ['15', '13 76 46 15 50 98 93 77 31 43 84 90 6 24 14']
        lines_export = [3]
    return lines_input, lines_export

def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        return 0
    else:
        return int(args[1])

def main():
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines(2)
    else:
        lines_input, lines_export = get_testdata(mode)
    result = abc173_a(lines_input)
    for v in result:
        print(v)
    if mode > 0:
        print(f'lines_input=[{lines_input}]')
        print(f'lines_export=[{lines_export}]')
        print(f'lines_result=[{result}]')
        if result == lines_export:
            print('OK')
        else:
            print('NG')

if __name__ == '__main__':
    main()