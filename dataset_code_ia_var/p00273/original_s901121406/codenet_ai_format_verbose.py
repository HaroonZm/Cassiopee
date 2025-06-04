number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):

    fixed_cost_per_book, fixed_cost_per_pen, number_of_books, number_of_pens = map(int, raw_input().split())

    total_cost_without_discount = fixed_cost_per_book * number_of_books + fixed_cost_per_pen * number_of_pens

    discounted_books_count = max(number_of_books, 5)
    discounted_pens_count = max(number_of_pens, 2)
    total_cost_with_discount = (fixed_cost_per_book * discounted_books_count + fixed_cost_per_pen * discounted_pens_count) * 0.8

    minimum_total_cost = min(total_cost_without_discount, total_cost_with_discount)

    print "%d" % minimum_total_cost