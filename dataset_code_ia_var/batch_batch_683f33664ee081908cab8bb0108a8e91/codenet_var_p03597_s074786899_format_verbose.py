import numpy as np

entered_square_side_length = int(input())
entered_area_to_subtract = int(input())

calculated_square_area = entered_square_side_length * entered_square_side_length

final_area_result = calculated_square_area - entered_area_to_subtract

print(final_area_result)