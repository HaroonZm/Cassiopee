import sys
from collections import deque, defaultdict

def solve():
    input = sys.stdin.readline
    while True:
        m,c,n = map(int,input().split())
        if m==0 and c==0 and n==0:
            break
        students = []
        total_requests = 0
        for _ in range(n):
            k = int(input())
            reqs = list(map(int,input().split()))
            students.append(deque(reqs))
            total_requests += k

        # Each desk is a list holding up to c books, initially empty
        desks = [[] for _ in range(m)]
        # shelf is all books not on any desk (including initially all books)
        shelf = set()
        # We don't know initial books; all requested books are on shelf initially.
        # So for now shelf contains all books in any request (unique)
        all_books = set()
        for s in students:
            all_books.update(s)
        shelf = set(all_books)

        # For quick lookup of where a book is:
        # book_location: book_id -> loc
        # loc=0..m-1 means desk index, m means shelf
        book_location = dict()
        for b in shelf:
            book_location[b] = m

        # For LRU tracking on D1 desk (desk 0):
        # We'll keep a list of books in order of last use, MRU at end, LRU at start
        # On each request of a book on D1, update LRU to move it to MRU
        d1_lru = deque()

        # Queue of students indexes who have outstanding requests
        queue = deque(i for i in range(n) if students[i])

        cost = 0

        def access_desk(d):
            # cost = d+1
            return d+1

        def access_shelf():
            return m+1

        def put_book_on_desk(d, b):
            desks[d].append(b)
            book_location[b] = d

        def remove_book_from_desk(d, b):
            desks[d].remove(b)
            book_location[b] = m

        def find_nonfull_desk(start, exclude = None):
            # start=0 means from D1 to Dm, but for temp placement:
            # We want closest to entrance that is not full
            # If exclude is not None, exclude that desk index
            for i in range(m):
                if i == exclude:
                    continue
                if len(desks[i])<c:
                    return i
            return None

        def find_lru_on_d1():
            # LRU book is leftmost in d1_lru
            if d1_lru:
                return d1_lru[0]
            return None

        def update_lru(book):
            # Move book to MRU (end of d1_lru)
            try:
                d1_lru.remove(book)
            except:
                pass
            d1_lru.append(book)

        for _ in range(total_requests):
            i = queue.popleft()
            book = students[i].popleft()

            loc = book_location.get(book, m) # default shelf
            # librarian finds book from D1..Dm, then shelf
            # cost for taking book:
            if loc == m:
                cost += access_shelf()
            else:
                cost += access_desk(loc)
            # After taking book out, book is removed from its current location
            if loc == m:
                shelf.remove(book)
            else:
                remove_book_from_desk(loc, book)
                if loc == 0:
                    # removed from D1, remove from LRU
                    try:
                        d1_lru.remove(book)
                    except:
                        pass

            # After giving copy, put book back on D1 according to rules

            if len(desks[0]) < c:
                # put requested book on D1 directly
                put_book_on_desk(0, book)
                update_lru(book)
                cost += access_desk(0)
            else:
                # D1 full
                # temp place requested book on closest non-full desk or shelf
                temp_d = find_nonfull_desk(0)
                temp_on_shelf = False
                if temp_d is None:
                    # all desks full
                    shelf.add(book)
                    book_location[book] = m
                    cost += access_shelf()
                    temp_on_shelf = True
                else:
                    put_book_on_desk(temp_d, book)
                    cost += access_desk(temp_d)

                # find LRU book on D1 and take it out
                lru_book = find_lru_on_d1()
                # remove lru_book from D1
                remove_book_from_desk(0, lru_book)
                d1_lru.popleft()
                cost += access_desk(0)

                # put lru_book on closest non-full desk except D1 or shelf
                lru_d = find_nonfull_desk(0, exclude=0)
                if lru_d is None:
                    shelf.add(lru_book)
                    book_location[lru_book] = m
                    cost += access_shelf()
                else:
                    put_book_on_desk(lru_d, lru_book)
                    cost += access_desk(lru_d)

                # finally take requested book from temp and put on D1
                if temp_on_shelf:
                    # remove from shelf
                    shelf.remove(book)
                    cost += access_shelf()
                else:
                    remove_book_from_desk(temp_d, book)
                    cost += access_desk(temp_d)

                put_book_on_desk(0, book)
                update_lru(book)
                cost += access_desk(0)

            # If student has more requests, go to queue end
            if students[i]:
                queue.append(i)

        print(cost)

if __name__=="__main__":
    solve()