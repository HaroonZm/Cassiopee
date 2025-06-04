import sys

args = sys.argv
if len(args) == 1:
    mode = 0
else:
    mode = int(args[1])

if mode == 0:
    lines = []
    for _ in range(2):
        lines.append(input())
else:
    if mode == 1:
        lines = ['5', '1 3 4 5 7']
        lines_export = [2]
    elif mode == 2:
        lines = ['15', '13 76 46 15 50 98 93 77 31 43 84 90 6 24 14']
        lines_export = [3]

N = int(lines[0])
values = list(map(int, lines[1].split(' ')))
answer = 0
for i in range(N):
    if i % 2 == 0:
        if values[i] % 2 != 0:
            answer += 1

print(answer)

if mode > 0:
    print(f'lines_input=[{lines}]')
    print(f'lines_export=[{lines_export}]')
    print(f'lines_result=[[{answer}]]')
    if [answer] == lines_export:
        print('OK')
    else:
        print('NG')