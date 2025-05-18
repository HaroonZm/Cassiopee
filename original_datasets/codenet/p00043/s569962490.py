import sys

def pokakito(num_line):
    if not num_line and flag == 1:
        result_lis.append(check_num)
        return True
    for num in num_line:
        if three(num, num_line): return True
        if two(num, num_line): return True
        if straight(num, num_line): return True
    
def three(num, num_line):
    count = 0
    for check in num_line[:3]:
        if check == num:
            count += 1
    else:
        if count == 3:
            if pokakito(num_line[3:]): return True

def two(num, num_line):
    global flag
    count = 0
    for check in num_line[:2]:
        if check == num:
            count += 1
    else:
        if count == 2:
            flag += 1
            if pokakito(num_line[2:]): return True
            flag -= 1

def straight(num, num_line):
    num_lis = [num,num+1,num+2]
    for i in range(3):
        for check in num_lis:
            if check < 0 or (not check in num_line):
                for i in range(3):
                    num_lis[i] = num_lis[i]-1
                break
        else:
            for n in num_lis:
                index = 0
                while num_line:
                    if num_line[index] == n:
                        del num_line[index]
                        break
                    index += 1
            else:
                if pokakito(num_line): return True
            
flag = 0
result_lis = []
check_num = 0
for input_line in sys.stdin:
    for i in range(9):
        check_num = i+1
        input_line = input_line.rstrip()
        line = sorted(input_line + str(check_num))
        line = ''.join(line)
        index = line.find(str(check_num))
        if line[index:index+5] == str(check_num)*5:
            continue
        pokakito([int(char) for char in line])
        result = sorted([str(num) for num in result_lis])
        flag = 0
    else:
        if result_lis:
            print ' '.join(result)
        else:
            print 0
    flag = 0
    result_lis = []
    check_num = 0