import re

def testcase_ends():
    n = int(input())
    if n == 0:
        return 1

    patt = re.compile(r'\d+$')
    marks = []
    for i in range(n):
        marks.append(input().replace('-', ''))

    links = {}
    bares = []
    labels = {}

    for i in range(len(marks)):
        mark = marks[i]
        idx = i + 1

        if mark == '':
            bares.append(idx)
            continue

        has_v = False
        if mark.endswith('v'):
            has_v = True
            mark = mark[:-1]
            links[idx + 1] = idx

        m = patt.search(mark)
        if m:
            num_val = int(m.group())
            name = patt.sub('', mark)

            if num_val == 1:
                if name in labels:
                    links[idx] = labels[name]
                    del labels[name]
                if not has_v:
                    bares.append(idx)
            else:
                if name in labels:
                    links[idx] = labels[name]
                labels[name] = idx

    for b in bares:
        print(b)
        x = b
        while x in links:
            x = links[x]
            print(x)

    return 0

def main():
    while testcase_ends() == 0:
        pass

if __name__ == '__main__':
    main()