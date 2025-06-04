input_count = input()
input_values = map(int, ('+ ' + raw_input()).replace('+ ', '+').replace('- ', '-').split())
abs_values = [abs(val) for val in input_values]
index_list = filter(lambda idx: input_values[idx + 1] < 0, xrange(input_count - 1)) + [input_count - 1] * 2
for idx in xrange(1, input_count):
    input_values[idx] += input_values[idx - 1]
    abs_values[idx] += abs_values[idx - 1]
result_candidates = [
    abs_values[input_count - 1] - 2 * abs_values[index_list[i + 1]] + abs_values[index_list[i]] + input_values[index_list[i]]
    for i in xrange(len(index_list) - 1)
]
print max(result_candidates)