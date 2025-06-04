t = int(input())
chars_map = {
    '1': '.,!? ',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
for _ in range(t):
    s = input()
    res = []
    prev = ''
    count = 0
    for c in s:
        if c == '0':
            if count > 0 and prev in chars_map:
                chs = chars_map[prev]
                res.append(chs[(count - 1) % len(chs)])
            prev = ''
            count = 0
        else:
            if c == prev:
                count += 1
            else:
                if count > 0 and prev in chars_map:
                    chs = chars_map[prev]
                    res.append(chs[(count - 1) % len(chs)])
                prev = c
                count = 1
    if count > 0 and prev in chars_map:
        chs = chars_map[prev]
        res.append(chs[(count - 1) % len(chs)])
    print(''.join(res))