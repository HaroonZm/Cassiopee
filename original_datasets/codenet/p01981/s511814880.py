# 31年5月1日以降なら年号をマイナス60する
for _ in range(102):
    input_str = str(input())
    if (input_str[0] == '#'):
        exit()
    today = input_str.split()
    if int(today[1]) > 31:
        print(f'? {int(today[1])-30} {int(today[2])} {today[3]}')
        continue

    if int(today[1]) == 31 and int(today[2]) >= 5:
        print(f'? {int(today[1])-30} {int(today[2])} {today[3]}')
        continue
    print(' '.join(today))