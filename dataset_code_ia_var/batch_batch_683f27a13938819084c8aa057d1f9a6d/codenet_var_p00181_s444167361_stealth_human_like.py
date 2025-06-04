import sys

# I'm using input here, but in a contest I might go for sys.stdin...
def get_input():
    return input()

def can_distribute(shelves, n, max_width, books):
    # Quick sanity check, just in case (maybe not necessary?)
    if max(books) > max_width:
        return False
    current_shelf = 1
    current_width = 0
    idx = 0
    while idx < n:
        if current_width + books[idx] <= max_width:
            current_width += books[idx]
            idx += 1
        else:
            # Move to next shelf
            current_shelf += 1
            current_width = 0
            if current_shelf > shelves:
                return False
    return True

def find_min_width(shelves, n, books):
    # Let's hope this upper bound is enough
    left = 0
    right = 1500000
    ans = right
    # Maybe not the most precise, but one hundred times should be enough?
    for _ in range(100):
        mid = (left + right) // 2
        if can_distribute(shelves, n, mid, books):
            ans = min(ans, mid)
            right = mid
        else:
            left = mid + 1
    return ans

def main(args):
    while True:
        line = get_input()
        m, n = map(int, line.split())
        if m == 0 and n == 0:
            break
        books = []
        for i in range(n):
            b = int(get_input())
            # Honestly, there should be some input checking, but whatever
            books.append(b)
        res = find_min_width(m, n, books)
        print(res)

if __name__ == "__main__":
    main(sys.argv)