while True:
    try:
        coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3, coord_x4, coord_y4 = map(float, raw_input().split())
        delta_y1 = coord_y2 - coord_y1
        delta_y2 = coord_y4 - coord_y3
        delta_x1 = coord_x2 - coord_x1
        delta_x2 = coord_x4 - coord_x3
        dot_product = delta_y1 * delta_y2 + delta_x1 * delta_x2
        if abs(dot_product) < 1e-10:
            print "YES"
        else:
            print "NO"
    except:
        break