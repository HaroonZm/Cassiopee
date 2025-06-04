from collections import deque
import sys

def process():
    input = sys.stdin.readline
    while True:
        m,c,n = map(int,input().split())
        if m==0 and c==0 and n==0:
            break
        requests = []
        for _ in range(n):
            k = int(input())
            books = list(map(int,input().split()))
            requests.append(deque(books))
        # queue of students who still have requests
        queue = deque(i for i in range(n) if requests[i])
        # desks: list of lists, each desk holds books (IDs)
        desks = [[] for _ in range(m)]
        # shelf: holds books not in desks
        shelf = set()
        # initially no books in desks => all books are on shelf
        # get all unique books from requests
        all_books = set()
        for rq in requests:
            all_books.update(rq)
        shelf = all_books.copy()
        # For tracking which book is where: desk index 0..m-1 or shelf m
        book_pos = {}
        for b in shelf:
            book_pos[b] = m  # shelf index is m
        # For tracking usage order in D1: list of books in order of usage, most recent last
        d1_lst = []
        cost = 0
        while queue:
            i = queue.popleft()
            b = requests[i].popleft()
            # locate book b
            loc = book_pos[b]
            # librarian enters storeroom to find the book:
            # cost for finding book = access to desk or shelf once to take it
            cost += loc+1
            # remove book from its current place
            if loc == m:
                shelf.remove(b)
            else:
                desks[loc].remove(b)
            # Now check if D1 not full
            if len(desks[0]) < c:
                # put book on D1
                desks[0].append(b)
                book_pos[b] = 0
                # cost of putting book on D1
                cost += 1
                # update usage for D1 books
                # remove if exists & add to last (MRU)
                if b in d1_lst:
                    d1_lst.remove(b)
                d1_lst.append(b)
            else:
                # D1 full
                # temporarily put requested book on nearest non full desk to entrance (D1 excluded) or shelf if all full
                placed = False
                for d in range(1,m):
                    if len(desks[d]) < c:
                        desks[d].append(b)
                        book_pos[b] = d
                        cost += d+1
                        placed=True
                        break
                if not placed:
                    # put on shelf
                    shelf.add(b)
                    book_pos[b] = m
                    cost += m+1
                # find LRU book on D1
                # d1_lst stores usage order, first is LRU
                lru = d1_lst.pop(0)
                # remove LRU book from D1
                desks[0].remove(lru)
                book_pos[lru] = None
                # put lru on nearest non full desk except D1 or shelf if all full
                placed = False
                for d in range(1,m):
                    if len(desks[d]) < c:
                        desks[d].append(lru)
                        book_pos[lru] = d
                        cost += d+1
                        placed=True
                        break
                if not placed:
                    shelf.add(lru)
                    book_pos[lru] = m
                    cost += m+1
                # take requested book back from its temporary place
                loc2 = book_pos[b]
                cost += loc2+1
                if loc2 == m:
                    shelf.remove(b)
                else:
                    desks[loc2].remove(b)
                # put requested book on D1
                desks[0].append(b)
                book_pos[b] = 0
                cost += 1
                # update usage list
                d1_lst.append(b)
            # if student still has requests, add at end of queue
            if requests[i]:
                queue.append(i)
        print(cost)

if __name__=="__main__":
    process()