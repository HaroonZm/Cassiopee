def get_input():
    return list(input())

def get_operators():
    return ['+','-']

def to_int(s):
    return int(s)

def calc(a, b, operator):
    if operator == '+':
        return a + b
    else:
        return a - b

def build_expression(num, op1, op2, op3):
    return num[0]+op1+num[1]+op2+num[2]+op3+num[3]+"=7"

def print_and_exit(ans):
    print(ans)
    exit()

def process_op3(res2, num, op1, op2, op3):
    res3 = calc(res2, to_int(num[3]), op3)
    if res3 == 7:
        ans = build_expression(num, op1, op2, op3)
        print_and_exit(ans)

def process_op2(res1, num, op1, op2, op_list):
    res2 = calc(res1, to_int(num[2]), op2)
    for op3 in op_list:
        process_op3(res2, num, op1, op2, op3)

def process_op1(num, op1, op_list):
    res1 = calc(to_int(num[0]), to_int(num[1]), op1)
    for op2 in op_list:
        process_op2(res1, num, op1, op2, op_list)

def main():
    num = get_input()
    op_list = get_operators()
    for op1 in op_list:
        process_op1(num, op1, op_list)

main()