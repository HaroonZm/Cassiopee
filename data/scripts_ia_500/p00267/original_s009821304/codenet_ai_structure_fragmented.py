def counting_sort_initialize_frequency(nmax):
	return [0] * (nmax + 1)

def counting_sort_fill_frequency(frequency_list, data_list):
	max_value = 0
	for value in data_list:
		frequency_list[value] += 1
		if value > max_value:
			max_value = value
	return max_value

def counting_sort_reconstruct_list(frequency_list, max_value, length):
	sorted_list = []
	remaining = length
	current_value = max_value
	while remaining > 0:
		count = frequency_list[current_value]
		if count > 0:
			sorted_list += [current_value] * count
			remaining -= count
		current_value -= 1
	return sorted_list

def counting_sort(nmax, data_list):
	frequency_list = counting_sort_initialize_frequency(nmax)
	max_value = counting_sort_fill_frequency(frequency_list, data_list)
	sorted_list = counting_sort_reconstruct_list(frequency_list, max_value, len(data_list))
	return sorted_list

def input_read_integer():
	return int(input())

def input_read_integer_list():
	return list(map(int, input().split()))

def process_single_case(n, list_a, list_b):
	sorted_a = counting_sort(100000, list_a)
	sorted_b = counting_sort(100000, list_b)
	answer = n
	index_b = -1
	for index_a in range(0, n, 2):
		index_b += 1
		if sorted_a[index_a] > sorted_b[index_b]:
			answer = index_a + 1
			break
	return answer

def print_answer(answer, n):
	if answer == n:
		print("NA")
	else:
		print(answer)

def main_loop():
	while True:
		n = input_read_integer()
		if n == 0:
			break
		a = input_read_integer_list()
		b = input_read_integer_list()
		answer = process_single_case(n, a, b)
		print_answer(answer, n)

main_loop()