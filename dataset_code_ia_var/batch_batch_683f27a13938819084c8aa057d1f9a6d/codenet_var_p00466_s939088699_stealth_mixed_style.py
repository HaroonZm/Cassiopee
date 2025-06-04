def process():
    from functools import reduce
    while 1:
        st = input()
        if st == '':
            break
        x = st
        def collect(n, acc):
            if n == 0:
                return acc
            else:
                y = input()
                return collect(n-1, acc + [y])
        result = x
        for val in collect(9, []):
            # mix dynamic typing: try to convert if possible
            try:
                result = int(result)-int(val)
            except:
                try:
                    result = float(result)-float(val)
                except:
                    result = str(result).replace(val, '')
        print(result)
process()