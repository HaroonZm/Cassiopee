num_books = int(input())
book_list = [input().split(" ") for book_idx in range(num_books)]
num_queries = int(input())
query_list = [input().split(" ") for query_idx in range(num_queries)]

book_date_list = []
for book_title, book_author, book_date_str in book_list:
    book_date_list.append(list(map(int, book_date_str.split("/"))))

def get_title_mask(search_title, book_list_ref):
    if search_title == "*":
        return (1 << (num_books + 1)) - 1
    result_mask = 0
    for idx, book_data in enumerate(book_list_ref):
        if search_title in book_data[0]:
            result_mask |= 1 << idx
    return result_mask

def get_author_mask(search_author, book_list_ref):
    if search_author == "*":
        return (1 << (num_books + 1)) - 1
    result_mask = 0
    for idx, book_data in enumerate(book_list_ref):
        if search_author in book_data[1]:
            result_mask |= 1 << idx
    return result_mask

def get_date_from_mask(search_date_from, date_list_ref):
    if search_date_from == "*":
        return (1 << (num_books + 1)) - 1
    result_mask = 0
    year_from, month_from, day_from = map(int, search_date_from.split("/"))
    for idx, (year, month, day) in enumerate(date_list_ref):
        if year > year_from or (year == year_from and month > month_from) or (year == year_from and month == month_from and day >= day_from):
            result_mask |= 1 << idx
    return result_mask

def get_date_to_mask(search_date_to, date_list_ref):
    if search_date_to == "*":
        return (1 << (num_books + 1)) - 1
    result_mask = 0
    year_to, month_to, day_to = map(int, search_date_to.split("/"))
    for idx, (year, month, day) in enumerate(date_list_ref):
        if year < year_to or (year == year_to and month < month_to) or (year == year_to and month == month_to and day <= day_to):
            result_mask |= 1 << idx
    return result_mask

for query_idx, query_data in enumerate(query_list):
    query_title, query_author, query_date_from, query_date_to = query_data
    title_mask = get_title_mask(query_title, book_list)
    author_mask = get_author_mask(query_author, book_list)
    date_from_mask = get_date_from_mask(query_date_from, book_date_list)
    date_to_mask = get_date_to_mask(query_date_to, book_date_list)
    combined_mask = title_mask & author_mask & date_from_mask & date_to_mask
    for book_idx in range(num_books):
        if combined_mask & 1:
            print(book_list[book_idx][0])
        combined_mask >>= 1
    if query_idx != num_queries - 1:
        print()