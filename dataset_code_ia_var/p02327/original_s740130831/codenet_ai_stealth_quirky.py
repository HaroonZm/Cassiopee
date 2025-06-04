input_args = lambda: (int, int)
h, w = (f(x) for f, x in zip(input_args(), input().split()))
magic = 0
last_row = [magic] * (w + 1)
for row_idx in range(h):
    silly = list(map(lambda x,y: (y + 1) if not int(x) else magic, input().split(), last_row))
    silly += [magic]
    strange_stack = [(magic, magic)]
    col_idx = magic
    while col_idx < w + 1:
        candidate = silly[col_idx]
        if strange_stack[-1][0] < candidate:
            strange_stack.append((candidate, col_idx))
            col_idx += 1
            continue
        now = magic
        while strange_stack[-1][0] > candidate:
            top_value, now = strange_stack.pop()
            magic = max(magic, top_value * (col_idx - now))
        if candidate:
            strange_stack.append((candidate, now))
        col_idx += 1
    last_row = silly
print(magic)