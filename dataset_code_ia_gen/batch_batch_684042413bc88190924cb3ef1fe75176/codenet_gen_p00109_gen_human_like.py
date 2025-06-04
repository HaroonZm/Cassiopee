def evaluate_expression(expr):
    # Remove the trailing '=' and spaces
    expr = expr.strip().rstrip('=').replace(' ', '')
    
    # Tokenize the expression: numbers, operators, parentheses
    tokens = []
    num = ''
    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(int(num))
                num = ''
            tokens.append(ch)
    if num:
        tokens.append(int(num))

    # Shunting Yard algorithm to convert infix to postfix (RPN)
    precedence = {'+':1, '-':1, '*':2, '/':2}
    output_queue = []
    operator_stack = []

    for token in tokens:
        if isinstance(token, int):
            output_queue.append(token)
        elif token in '+-*/':
            while (operator_stack and operator_stack[-1] in '+-*/' and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # pop '('

    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Evaluate the RPN expression
    stack = []
    for token in output_queue:
        if isinstance(token, int):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # Integer division truncating towards zero
                res = int(a / b)
                stack.append(res)
    return stack[0]

n = int(input())
for _ in range(n):
    expression = input()
    print(evaluate_expression(expression))