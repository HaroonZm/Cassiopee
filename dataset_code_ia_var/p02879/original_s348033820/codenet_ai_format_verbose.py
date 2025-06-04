first_integer, second_integer = map(int, input().split())

maximum_of_integers = max(first_integer, second_integer)

if maximum_of_integers <= 9:
    product_of_integers = first_integer * second_integer
    print(product_of_integers)
else:
    print(-1)