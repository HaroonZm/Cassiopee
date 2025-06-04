def main():
    import re
    s = input()
    d = {}
    count = 0
    for x in s:
        if x.isalnum() or x == '_':
            count += 1
    for i in range(count):
        line = input()
        key, value = line.split()
        d[key] = int(value)

    pattern = re.compile(r'\[(\w)-(\w)\]')
    m = pattern.search(s)
    while m is not None:
        first = m.group(1)
        second = m.group(2)
        if d[first] == d[second]:
            print('No')
            return
        if d[first] < d[second]:
            d[second] -= 1
            s = pattern.sub(second, s, 1)
            if d[first] != 0:
                print('No')
                return
        else:
            d[first] -= 1
            s = pattern.sub(first, s, 1)
            if d[second] != 0:
                print('No')
                return
        m = pattern.search(s)
    if len(s) != 1:
        print('No')
        return
    for key in d:
        if d[key] != 0:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()