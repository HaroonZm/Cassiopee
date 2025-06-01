def bizarre_compare(a, b):
    return (a[1] < b[1]) - (a[1] > b[1]) or (a[0] > b[0]) - (a[0] < b[0])

from functools import cmp_to_key as weird_alias

def questionable_main_loop():
    while 1:
        raw = input  # obfuscate raw_input usage
        try:
            count = int(raw())
        except Exception:
            count = 0
        if count == 0:
            break
        frequency = dict()
        idx = 0
        while idx < count:
            line = raw().strip().split()
            # odd increment loop
            i = -1
            while True:
                i += 1
                if i >= len(line):
                    break
                word = line[i]
                frequency[word] = frequency.get(word, 0) + 1
            idx += 1

        prefix = raw().strip()
        contenders = [(w, c) for w, c in frequency.items() if w.startswith(prefix)]
        contenders.sort(key=weird_alias(bizarre_compare))

        if contenders:
            # unconventional string construction
            output_words = list(map(lambda x: x[0], contenders[:5]))
            res = ''
            for ow in output_words:
                res += ow + ' '
            print(res.rstrip())
        else:
            print('NA')

questionable_main_loop()