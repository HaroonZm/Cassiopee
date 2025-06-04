expression = input()
bob_answer = int(input())

# Calcul multiplication avant addition
def calc_mul_first(expr):
    nums = []
    ops = []
    for i in range(len(expr)):
        if i % 2 == 0:
            nums.append(int(expr[i]))
        else:
            ops.append(expr[i])
    # Calcul les multiplications en premier
    new_nums = [nums[0]]
    new_ops = []
    for i in range(len(ops)):
        if ops[i] == '*':
            new_nums[-1] = new_nums[-1] * nums[i+1]
        else:
            new_ops.append(ops[i])
            new_nums.append(nums[i+1])
    # Puis additions
    result = new_nums[0]
    for i in range(len(new_ops)):
        result += new_nums[i+1]
    return result

# Calcul de gauche à droite
def calc_left_to_right(expr):
    result = int(expr[0])
    for i in range(1, len(expr), 2):
        op = expr[i]
        num = int(expr[i+1])
        if op == '+':
            result += num
        else:
            result *= num
    return result

m = calc_mul_first(expression)
l = calc_left_to_right(expression)

if m == bob_answer and l == bob_answer:
    print('U')
elif m == bob_answer:
    print('M')
elif l == bob_answer:
    print('L')
else:
    print('I')