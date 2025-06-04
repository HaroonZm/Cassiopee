num_books = int(input())
book_list = [input().split() for _ in range(num_books)]
num_queries = int(input())
for query_index in range(num_queries):
    filter_title, filter_author, filter_date_from, filter_date_to = input().split()
    for book_title, book_author, book_date in book_list:
        title_match = filter_title == "*" or filter_title in book_title
        author_match = filter_author == "*" or filter_author in book_author
        date_from_match = filter_date_from == "*" or filter_date_from <= book_date
        date_to_match = filter_date_to == "*" or book_date <= filter_date_to
        if title_match and author_match and date_from_match and date_to_match:
            print(book_title)
    if query_index != num_queries - 1:
        print()