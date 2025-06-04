count_elements = int(input())
list_elements = list(map(int, input().split()))
sum_elements = sum(list_elements)
for index_element in range(count_elements):
    value_element = list_elements[index_element]
    if 2 * value_element < sum_elements:
        continue
    else:
        print('No')
        break
else:
    print('Yes')