def eval_expr(lines, start, level):
    # Get current line and level
    line = lines[start]
    count_dot = 0
    while count_dot < len(line) and line[count_dot] == '.':
        count_dot += 1
    cur_level = count_dot
    content = line[count_dot:]
    if cur_level != level:
        return None, start
    if content.isdigit():
        # It's a single digit integer
        return int(content), start + 1
    else:
        # It's an operator
        op = content
        vals = []
        pos = start + 1
        while True:
            if pos >= len(lines):
                break
            # Check next line level
            next_line = lines[pos]
            cnt = 0
            while cnt < len(next_line) and next_line[cnt] == '.':
                cnt += 1
            if cnt != level + 1:
                break
            val, nxt = eval_expr(lines, pos, level + 1)
            vals.append(val)
            pos = nxt
        if op == '+':
            return sum(vals), pos
        else:
            res = 1
            for v in vals:
                res *= v
            return res, pos

while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    lines = [input() for _ in range(n)]
    val, _ = eval_expr(lines, 0, 0)
    print(val)