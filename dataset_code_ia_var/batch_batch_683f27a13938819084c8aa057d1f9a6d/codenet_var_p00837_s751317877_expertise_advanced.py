from sys import stdin
from collections import deque, defaultdict

def solve():
    input_iter = iter(stdin.readline, '')
    results = []

    while True:
        try:
            m, c, n = map(int, next(input_iter).split())
        except StopIteration:
            break
        if m == 0:
            break

        shelf = m + 1
        book_location = {}
        students = deque()
        for _ in range(n):
            k = int(next(input_iter))
            books = deque(map(int, next(input_iter).split()))
            for b in books:
                book_location[b] = shelf
            students.append(books)

        desk_counts = [0] * (m + 2)
        first_desk = deque()
        cost = 0
        available_desks = set(range(2, m + 1))

        while students:
            curr_books = students.popleft()
            book = curr_books.popleft()
            loc = book_location[book]
            cost += loc

            if loc == 1:
                first_desk.remove(book)
            elif loc != shelf:
                desk_counts[loc] -= 1
                if desk_counts[loc] == c - 1:
                    available_desks.add(loc)

            if len(first_desk) == c:
                # Place requested book
                for desk_idx in sorted(available_desks):
                    if desk_counts[desk_idx] < c:
                        desk_counts[desk_idx] += 1
                        if desk_counts[desk_idx] == c:
                            available_desks.remove(desk_idx)
                        book_location[book] = desk_idx
                        cost += desk_idx
                        place = desk_idx
                        break
                else:
                    book_location[book] = shelf
                    cost += shelf
                    place = shelf

                unreq_book = first_desk.popleft()
                cost += 1
                # Place unrequested book
                if place == shelf:
                    book_location[unreq_book] = shelf
                    cost += shelf
                else:
                    for desk_idx in sorted(available_desks):
                        if desk_counts[desk_idx] < c:
                            desk_counts[desk_idx] += 1
                            if desk_counts[desk_idx] == c:
                                available_desks.remove(desk_idx)
                            book_location[unreq_book] = desk_idx
                            cost += desk_idx
                            break
                    else:
                        book_location[unreq_book] = shelf
                        cost += shelf
                # Move requested book to first desk
                if place != shelf:
                    desk_counts[place] -= 1
                    if desk_counts[place] == c - 1:
                        available_desks.add(place)
                first_desk.append(book)
                book_location[book] = 1
                cost += (place + 1)
            else:
                first_desk.append(book)
                book_location[book] = 1
                cost += 1

            if curr_books:
                students.append(curr_books)

        results.append(str(cost))

    print('\n'.join(results))

solve()