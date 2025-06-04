number_of_elements_in_first_set = int(input())

first_set_elements = set(
    list(
        map(
            int,
            input().split()
        )
    )
)

number_of_elements_in_second_set = int(input())

second_set_elements = set(
    list(
        map(
            int,
            input().split()
        )
    )
)

elements_unique_to_first_set = first_set_elements - second_set_elements

for unique_element in sorted(elements_unique_to_first_set):
    print(unique_element)