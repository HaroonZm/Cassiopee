import numpy as np

def get_canvas_dimensions(H, W):
    height = 2 * W + 1
    width = 2 * (H + H + 1)
    return height, width

def create_canvas(height, width):
    return np.full((height, width), '.', dtype='U1')

def get_left_view(X, H):
    return X[:, :H + H + 1]

def get_right_view(X, H):
    return X[:, H + H + 1:]

def fill_right_with_symbol(right, symbol='#'):
    right[:] = symbol

def process_params():
    A, B = map(int, input().split())
    return A, B

def get_symbol_table(A,B):
    return [
        ['#', B - 1, 'left'],
        ['.', A - 1, 'right'],
    ]

def assign_view(view_name, X, H):
    if view_name == 'left':
        return get_left_view(X, H)
    else:
        return get_right_view(X, H)

def fill_region(symbol, n, view, H):
    q, r = n // H, n % H
    fill_full_blocks(view, q, symbol)
    fill_remaining(view, q, r, symbol)

def fill_full_blocks(view, q, symbol):
    for i in range(q):
        view[2 * i + 1, 1::2] = symbol

def fill_remaining(view, q, r, symbol):
    view[2 * q + 1, 1:1 + 2 * r:2] = symbol

def print_dimensions(W, H):
    print(2 * W + 1, 4 * H + 2)

def print_canvas(X):
    for row in X:
        print(''.join(row))

def main():
    H = 24
    W = 49
    height, width = get_canvas_dimensions(H, W)
    X = create_canvas(height, width)
    A, B = process_params()
    left = get_left_view(X, H)
    right = get_right_view(X, H)
    fill_right_with_symbol(right, '#')
    symbol_table = get_symbol_table(A, B)
    for symbol, n, view_name in symbol_table:
        view = assign_view(view_name, X, H)
        fill_region(symbol, n, view, H)
    print_dimensions(W, H)
    print_canvas(X)

main()