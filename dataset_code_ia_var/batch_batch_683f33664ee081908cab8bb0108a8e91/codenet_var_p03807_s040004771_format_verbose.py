number_of_elements = int(input())

input_elements = list(map(int, input().split()))

list_of_parities = list(map(lambda element: element % 2, input_elements))

count_of_odd_numbers = list_of_parities.count(1)

if count_of_odd_numbers % 2 == 0:
    print('YES')
else:
    print('NO')