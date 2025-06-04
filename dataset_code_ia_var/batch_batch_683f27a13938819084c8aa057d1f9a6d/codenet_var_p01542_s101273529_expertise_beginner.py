import sys

def read_list_int():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_list_str():
    return sys.stdin.readline().split()

def read_str_line():
    return list(sys.stdin.readline().strip())

def main():
    def dfs(depth, current):
        if depth == len(s):
            exprs.append(current)
        else:
            if s[depth] == ".":
                for i in range(2):
                    dfs(depth + 1, current + [str(i)])
                for op in "+-*()":
                    dfs(depth + 1, current + [op])
            else:
                dfs(depth + 1, current + [s[depth]])

    def calc(op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b

    def parse_expr(seq, idx):
        if idx == float("inf"):
            return -1, float("inf")
        has_parenthesis = False
        if idx > 0 and seq[idx - 1] == "(":
            has_parenthesis = True

        total, idx_now, num_ops = parse_term(seq, idx, 0)
        while idx_now < len(seq) and seq[idx_now] in "+-":
            num_ops += 1
            op, idx_now_op = parse_op(seq, idx_now)
            item, idx_now, num_ops = parse_term(seq, idx_now_op, num_ops)
            total = calc(op, total, item)
            if total >= 1024 or total < 0:
                return -1, float("inf")
        if has_parenthesis and not num_ops:
            return -1, float("inf")
        return total, idx_now

    def parse_term(seq, idx, num_ops):
        factor, idx_now = parse_factor(seq, idx)
        while idx_now < len(seq) and seq[idx_now] == "*":
            num_ops += 1
            op, idx_now_op = parse_op(seq, idx_now)
            factor2, idx_now = parse_factor(seq, idx_now_op)
            factor = calc(op, factor, factor2)
            if factor >= 1024 or factor < 0:
                return -1, float("inf"), num_ops
        return factor, idx_now, num_ops

    def parse_op(seq, idx):
        return seq[idx], idx + 1

    def parse_factor(seq, idx):
        if idx >= len(seq):
            return -1, float("inf")
        if seq[idx] == "(":
            idx += 1
            res, idx = parse_expr(seq, idx)
            if idx >= len(seq) or seq[idx] != ")":
                return -1, float("inf")
            idx += 1
            return res, idx
        else:
            if not seq[idx].isdigit():
                return -1, float("inf")
            num = int(seq[idx])
            idx += 1
            while idx < len(seq) and seq[idx].isdigit():
                num = num * 2 + int(seq[idx])
                idx += 1
            if num >= 1024 or num < 0:
                return -1, float("inf")
            return num, idx

    s = read_str_line()
    exprs = []
    dfs(0, [])
    max_val = -1
    for seq in exprs:
        value, idx_end = parse_expr(seq, 0)
        if idx_end == len(seq):
            if value > max_val:
                max_val = value
    print(max_val)

if __name__ == "__main__":
    main()