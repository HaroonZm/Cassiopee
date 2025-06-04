input_list_a = [int(input()) for input_index_a in range(10)]
top_elements_a = sorted(input_list_a, reverse=True)[:3]
sum_top_a = sum(top_elements_a)

input_list_b = [int(input()) for input_index_b in range(10)]
top_elements_b = sorted(input_list_b, reverse=True)[:3]
sum_top_b = sum(top_elements_b)

print(sum_top_a, end=' ')
print(sum_top_b)