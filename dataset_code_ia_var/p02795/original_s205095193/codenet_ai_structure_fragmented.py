def get_input(prompt):
    return int(input(prompt))

def initialize_variables():
    H = get_input('')
    W = get_input('')
    N = get_input('')
    return H, W, N

def should_paint_width_first(W, H):
    return W > H

def update_state_width(W, H, count, paint):
    count += 1
    paint += W
    H -= 1
    return H, W, count, paint

def update_state_height(W, H, count, paint):
    count += 1
    paint += H
    W -= 1
    return H, W, count, paint

def painting_loop(H, W, N):
    count = 0
    paint = 0
    while paint < N:
        if should_paint_width_first(W, H):
            H, W, count, paint = update_state_width(W, H, count, paint)
        else:
            H, W, count, paint = update_state_height(W, H, count, paint)
    return count

def output_result(count):
    print(count)

def main():
    H, W, N = initialize_variables()
    count = painting_loop(H, W, N)
    output_result(count)

main()