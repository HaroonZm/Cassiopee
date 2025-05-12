import fileinput

chr_master = [
    ' ', '\',.!?', 'abcABC', 'defDEF', 'ghiGHI',
    'jklJKL', 'mnoMNO', 'pqrsPQRS', 'tuvTUV', 'wxyzWXYZ'
]

for s in (line.strip() for line in fileinput.input()):
    s += '!'
    prev_c = None
    cnt = 0
    chr_list = []
    for c in s:
        if c == prev_c:
            cnt += 1
            continue
        if prev_c == '0':
            if cnt > 1:
                chr_list.extend([(0, 0)] * (cnt - 1))
        else:
            if prev_c is not None:
                chr_list.append((int(prev_c), cnt - 1))

        prev_c = c
        cnt = 1
    print(''.join(chr_master[i][j] for i, j in chr_list))