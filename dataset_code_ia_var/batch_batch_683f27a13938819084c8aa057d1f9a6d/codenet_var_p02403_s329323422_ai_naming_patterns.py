while True:
    try:
        input_height, input_width = map(int, raw_input().split())
        if input_height == 0 and input_width == 0:
            break
        for row_index in xrange(input_height):
            print ''.join(['#' for col_index in xrange(input_width)])
        print
    except EOFError:
        break