first_number, second_number = map(int, raw_input().split())
product_result = first_number * second_number
perimeter_result = (first_number + second_number) * 2
print "%d %d" % (product_result, perimeter_result)