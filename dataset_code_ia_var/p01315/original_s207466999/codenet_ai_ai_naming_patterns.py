import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class MainProcessor(object):

    def __init__(self):
        pass

    def execute(self):
        while True:
            input_count = input()
            if input_count == 0:
                break
            item_list = []
            for item_index in range(input_count):
                input_line = raw_input()
                tokens = input_line.split()
                label = tokens[0]
                param_p, param_a, param_b, param_c, param_d, param_e, param_f, param_s, param_m = map(int, tokens[1:])
                calculated_efficiency = 1.0 * (param_f * param_s * param_m - param_p) / (param_a + param_b + param_c + param_m * (param_d + param_e))
                item_list.append((calculated_efficiency, label))
            item_list.sort(key=lambda tuple_item: (-tuple_item[0], tuple_item[1]))
            for efficiency_item in item_list:
                print efficiency_item[1]
            print '#'
        return None

if __name__ == '__main__':
    main_processor_instance = MainProcessor()
    main_processor_instance.execute()