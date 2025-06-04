MODULO_VALUE = 100000007

def combination_dp(total_items, selected_items):
    if combination_table[total_items][selected_items]:
        return combination_table[total_items][selected_items]
    if (selected_items << 1) > total_items:
        selected_items = total_items - selected_items
    if selected_items == 0:
        result_value = 1
    elif selected_items == 1:
        result_value = total_items
    else:
        result_value = combination_dp(total_items - 1, selected_items) + combination_dp(total_items - 1, selected_items - 1)
    combination_table[total_items][selected_items] = result_value % MODULO_VALUE
    return combination_table[total_items][selected_items]

combination_table = [[0 for col_index in range(1001)] for row_index in range(1001)]

duplication_count = 0
row_count, column_count, coord_a_row, coord_a_col, coord_b_row, coord_b_col = map(int, input().split())

delta_row = abs(coord_a_row - coord_b_row)
if delta_row > row_count - delta_row:
    delta_row = row_count - delta_row
if (delta_row << 1) == row_count:
    duplication_count += 1

delta_col = abs(coord_a_col - coord_b_col)
if delta_col > column_count - delta_col:
    delta_col = column_count - delta_col
if (delta_col << 1) == column_count:
    duplication_count += 1

min_delta = min(delta_row, delta_col)
total_delta = delta_row + delta_col

result_output = (combination_dp(total_delta, min_delta) << duplication_count) % MODULO_VALUE
print(result_output)