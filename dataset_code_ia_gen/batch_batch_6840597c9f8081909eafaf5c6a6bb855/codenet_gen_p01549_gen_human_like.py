m = int(input())
vars_bounds = {}
for _ in range(m):
    name, lb, ub = input().split()
    vars_bounds[name] = (int(lb), int(ub))
n = int(input())
expr = input().split()

def is_operator(x):
    return x in ['+', '-', '*', '/']

# We will simulate the RPN evaluation with interval arithmetic.
# Each value on the stack is a tuple (min_val, max_val) representing
# the possible values that this element can take.
stack = []
for token in expr:
    if token.isdigit():
        v = int(token)
        stack.append((v, v))
    elif token in vars_bounds:
        stack.append(vars_bounds[token])
    elif is_operator(token):
        if len(stack) < 2:
            print("error")
            exit()
        b_min, b_max = stack.pop()
        a_min, a_max = stack.pop()

        # For each operator we compute the resulting interval
        if token == '+':
            res_min = (a_min + b_min) % 256
            res_max = (a_max + b_max) % 256
            # Addition modulo 256 can wrap around, so interval may wrap.
            # To be safe, we consider the possible full range if wrap may occur:
            # but to keep things simple, we consider the interval as the full range
            # if the normal interval crosses 256.
            # Here we compute all sums and find min and max mod 256:
            candidates = []
            for x in [a_min, a_max]:
                for y in [b_min, b_max]:
                    candidates.append((x + y) % 256)
            res_min = min(candidates)
            res_max = max(candidates)
            # But if max < min, means wrap, so full range possible
            if res_max < res_min:
                res_min, res_max = 0, 255
            stack.append((res_min,res_max))

        elif token == '-':
            # (a - b + 256) % 256
            candidates = []
            for x in [a_min, a_max]:
                for y in [b_min, b_max]:
                    candidates.append((x - y + 256) % 256)
            res_min = min(candidates)
            res_max = max(candidates)
            if res_max < res_min:
                res_min, res_max = 0, 255
            stack.append((res_min,res_max))

        elif token == '*':
            candidates = []
            for x in [a_min, a_max]:
                for y in [b_min, b_max]:
                    candidates.append((x * y) % 256)
            res_min = min(candidates)
            res_max = max(candidates)
            if res_max < res_min:
                res_min, res_max = 0, 255
            stack.append((res_min,res_max))

        elif token == '/':
            # Division: before checking, division by zero possible?
            if b_min <= 0 <= b_max:
                # zero in denominator range -> error
                print("error")
                exit()
            candidates = []
            for x in [a_min, a_max]:
                for y in [b_min, b_max]:
                    candidates.append((x // y) % 256)
            res_min = min(candidates)
            res_max = max(candidates)
            if res_max < res_min:
                res_min, res_max = 0, 255
            stack.append((res_min,res_max))

    else:
        # Unknown token
        print("error")
        exit()

if len(stack) != 1:
    print("error")
else:
    print("correct")