def read_input_line():
    try:
        return raw_input()
    except EOFError:
        return None

def parse_line(line):
    return map(int, line.split(','))

def process_entry(l, n, cnt):
    if n in l:
        l[n][0] += 1
        if cnt == 1:
            l[n][1] = 2
    elif cnt == 0:
        l[n] = [1, 1]

def should_stop(cnt):
    return cnt > 1

def collect_valid_entries(l):
    a = []
    for i in l:
        if l[i][1] == 2:
            a.append([i, l[i][0]])
    return a

def print_entries(a):
    for i in a:
        print i[0], i[1]

def main_loop():
    cnt = 0
    l = {}
    while True:
        line = read_input_line()
        if line is None:
            cnt += 1
            if should_stop(cnt):
                break
            else:
                continue
        try:
            n, k = parse_line(line)
            process_entry(l, n, cnt)
        except:
            cnt += 1
            if should_stop(cnt):
                break
    a = collect_valid_entries(l)
    a.sort()
    print_entries(a)

main_loop()