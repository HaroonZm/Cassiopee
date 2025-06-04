expression = input().strip()
bob_answer = int(input().strip())

# Parse numbers and operators
numbers = [int(expression[i]) for i in range(0, len(expression), 2)]
operators = [expression[i] for i in range(1, len(expression), 2)]

def calc_mul_first(nums, ops):
    # First perform all multiplications
    new_nums = []
    new_ops = []
    acc = nums[0]
    for i, op in enumerate(ops):
        if op == '*':
            acc *= nums[i+1]
        else:
            new_nums.append(acc)
            new_ops.append(op)
            acc = nums[i+1]
    new_nums.append(acc)
    # Then perform all additions
    result = new_nums[0]
    for i, op in enumerate(new_ops):
        if op == '+':
            result += new_nums[i+1]
    return result

def calc_left_to_right(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i+1]
        else:
            result *= nums[i+1]
    return result

mul_first_result = calc_mul_first(numbers, operators)
left_to_right_result = calc_left_to_right(numbers, operators)

mul_match = (mul_first_result == bob_answer)
left_match = (left_to_right_result == bob_answer)

if mul_match and left_match:
    print('U')
elif mul_match:
    print('M')
elif left_match:
    print('L')
else:
    print('I')