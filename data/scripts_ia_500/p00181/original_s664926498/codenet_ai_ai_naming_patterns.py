while True:
    total_columns, total_books = map(int, input().split())
    if total_columns + total_books == 0:
        break
    else:
        pages_per_book = [int(input()) for _ in range(total_books)]
        lower_bound = min(pages_per_book)
        upper_bound = 10**7
        while lower_bound < upper_bound:
            mid_value = (lower_bound + upper_bound) // 2
            required_columns = 1
            accumulated_pages = 0
            for pages in pages_per_book:
                if pages > mid_value:
                    required_columns = total_columns + 1
                    break
                accumulated_pages += pages
                if accumulated_pages > mid_value:
                    accumulated_pages = pages
                    required_columns += 1
            if required_columns > total_columns:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value
        print(lower_bound)