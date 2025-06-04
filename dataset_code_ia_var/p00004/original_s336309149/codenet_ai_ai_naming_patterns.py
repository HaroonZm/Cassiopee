#!/usr/bin/python3

while True:
    try:
        values_list = list(map(int, input().split()))
        numerator_x = values_list[1] * values_list[5] - values_list[2] * values_list[4]
        denominator_x = values_list[1] * values_list[3] - values_list[0] * values_list[4]
        result_x = numerator_x / denominator_x
        result_y = (values_list[2] - values_list[0] * result_x) / values_list[1]
        if result_x == 0:
            result_x = 0
        print("{0:.3f} {1:.3f}".format(result_x, result_y))
    except:
        break