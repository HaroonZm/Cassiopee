def evaluate_expression(lines):
    # Parse the input lines into a list of (level, content)
    expr = []
    for line in lines:
        level = 0
        while level < len(line) and line[level] == '.':
            level += 1
        content = line[level:]
        expr.append((level, content))

    # Recursive function to parse and evaluate expression starting at index i
    # Returns (value, next_index_to_process)
    def parse(i):
        level, content = expr[i]
        # if content is digit => integer operand
        if content.isdigit():
            return int(content), i + 1

        # else content is operator '+' or '*'
        op = content

        operands = []
        i += 1
        # all operands are expressions with level = current level + 1
        operand_level = level + 1
        # We gather all expressions that have operand_level == operand_level
        # as operands for this operator.
        # Since nesting is explicit through level, we parse operands one by one
        # until we find a line which level <= current level (which means end of operands)
        # or end of input.
        while i < len(expr) and expr[i][0] == operand_level:
            val, i = parse(i)
            operands.append(val)

        # apply operator
        if op == '+':
            return sum(operands), i
        else:
            prod = 1
            for v in operands:
                prod *= v
            return prod, i

    val, _ = parse(0)
    return val


def main():
    import sys
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        lines = [input().rstrip('\n') for _ in range(n)]
        print(evaluate_expression(lines))


if __name__ == "__main__":
    main()