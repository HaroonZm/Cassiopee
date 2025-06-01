def is_storage_capacity_feasible(max_capacity, num_books, max_shelves, book_sizes):
    current_index = 0
    current_capacity = 0
    shelves_used = 1
    while current_index < num_books:
        if shelves_used > max_shelves:
            return False
        if current_capacity + book_sizes[current_index] > max_capacity:
            shelves_used += 1
            current_capacity = 0
        else:
            current_capacity += book_sizes[current_index]
            current_index += 1
    return True

while True:
    max_shelves, num_books = map(int, raw_input().split())
    if max_shelves == 0:
        break
    book_sizes = [int(raw_input()) for _ in range(num_books)]
    max_capacity = sum(book_sizes) // 2
    step = max_capacity
    while step:
        step //= 2
        if is_storage_capacity_feasible(max_capacity, num_books, max_shelves, book_sizes):
            max_capacity -= step
        else:
            max_capacity += step
    max_capacity += 6
    while is_storage_capacity_feasible(max_capacity - 1, num_books, max_shelves, book_sizes):
        max_capacity -= 1
    print max_capacity