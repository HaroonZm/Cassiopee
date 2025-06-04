def process_books_query():
    num_books = int(input())
    book_list = []
    for book_idx in range(num_books):
        input_title, input_author, input_pub_date = input().split()
        parsed_pub_date = list(map(int, input_pub_date.split('/')))
        book_list.append((input_title, input_author, parsed_pub_date))

    num_queries = int(input())
    for query_idx in range(num_queries):
        query_title, query_author, query_date_from, query_date_to = input().split()

        if query_date_from != '*':
            parsed_date_from = list(map(int, query_date_from.split('/')))
        else:
            parsed_date_from = '*'

        if query_date_to != '*':
            parsed_date_to = list(map(int, query_date_to.split('/')))
        else:
            parsed_date_to = '*'

        filtered_books = book_list[:]
        filtered_books = [book_record for book_record in filtered_books if query_title == '*' or query_title in book_record[0]]
        filtered_books = [book_record for book_record in filtered_books if query_author == '*' or query_author in book_record[1]]
        filtered_books = [book_record for book_record in filtered_books if parsed_date_from == '*' or parsed_date_from <= book_record[2]]
        filtered_books = [book_record for book_record in filtered_books if parsed_date_to == '*' or parsed_date_to >= book_record[2]]

        for output_book in filtered_books:
            print(output_book[0])

        if query_idx + 1 < num_queries:
            print()

process_books_query()