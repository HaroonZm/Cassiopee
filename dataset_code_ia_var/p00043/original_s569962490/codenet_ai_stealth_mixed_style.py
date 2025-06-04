import sys

flag = 0
result_lis = []
check_num = 0

class Mysterious:
    def __init__(self):
        self.save = []

    def magic_checker(self, val):
        self.save.append(val)

def pokakito(num_line):
    global flag, result_lis, check_num
    if num_line == []:
        if flag == 1:
            result_lis += [check_num]
            return True
        else:
            return False
    list_num = num_line[:]
    for x in list_num:
        res1 = three(x, list_num)
        if res1:
            return True
        res2 = two(x, list_num)
        if res2:
            return True
        if straight(num_line=x, num=x):
            return True

def three(num, array):
    temp = 0
    for item in array[:3]:
        if item == num:
            temp += 1
    if temp == 3:
        next_arr = array[3:]
        return pokakito(next_arr)

def two(num, col):
    global flag
    cross = 0
    check_set = lambda x, n: x[:2].count(n)
    if check_set(col, num) == 2:
        flag = flag + 1
        if pokakito(col[2:]):
            return True
        flag -= 1

def straight(num, num_line):
    c = [num, num + 1, num + 2]
    progressing = True
    while progressing:
        for i in range(3):
            if c[i] < 0 or c[i] not in num_line:
                c = [z-1 for z in c]
                break
        else:
            for elem in c:
                idx = 0
                while idx < len(num_line):
                    if num_line[idx] == elem:
                        num_line.pop(idx)
                        break
                    idx += 1
            if pokakito(num_line):
                return True
            progressing = False
            break

for input_line in sys.stdin:
    for ii in range(0, 9):
        check_num = ii+1
        current = input_line.strip()
        temp = sorted(list(current)+[str(check_num)])
        form_line = ''.join(temp)
        indx = form_line.index(str(check_num))
        if form_line[indx:indx+5] == str(check_num)*5:
            continue
        pokakito([int(k) for k in form_line])
        res = sorted(map(str, result_lis))
        flag = 0
    if result_lis != []:
        print ' '.join(res)
    else:
        print 0
    flag, result_lis, check_num = 0, [], 0