import sys

def main():
    data = []
    for passwd in sys.stdin.readlines():
        data.append(passwd.strip())
    for answer in proc(data):
        print answer
    return 0

def proc(data):
    return [passwd for passwd in data if is_hitofude(passwd)]

def is_hitofude(text):
    for first, second in get_pair(text):
        if second == '': break
        if not _can_slide(first, second):
            return False
    return True

def get_pair(text):
    pair_list = list(text)
    pair_list.reverse()
    while(True):
        if 2 <= len(pair_list):
            yield (pair_list.pop(), pair_list[-1])
        elif 1 == len(pair_list):
            yield (pair_list.pop(), '')
        else:
            break

matrix = ["ABC",
          "DEF",
          "GHI"]
pair = []
for y, row in enumerate(matrix):
    for x, base in enumerate(row):
        if x+1 < len(row): pair.append((base, row[x+1])) #EF
        if 0 <= x-1 : pair.append((base, row[x-1])) #ED
        if y+1 < 3: pair.append((base, matrix[y+1][x])) #EH
        if 0 <= y-1: pair.append((base, matrix[y-1][x])) #EB

def _can_slide(first, second):
    return (first, second) in pair

if __name__ == '__main__':
    main()