def count(xs, ys):
    """Returns a count of elements in ys which is also in xs.
    - xs: a sequence of integers sorted in ascending order.
    - ys: a sequence of different integers.

    >>> count([1, 2, 3], [1, 3])
    2
    >>> count([1, 2, 3, 4, 5], [3, 4, 1])
    3
    >>> count([1, 2, 3], [5])
    0
    >>> count([1, 1, 2, 2, 3], [1, 2])
    2
    """
    def binsearch(i, j, n):
        while i <= j:
            mid = (i + j) // 2
            if xs[mid] > n:
                j = mid - 1
            elif xs[mid] < n:
                i = mid + 1
            else:
                return True

        return False

    return [binsearch(0, len(xs)-1, y) for y in ys].count(True)

def run():
    _ = input()  # flake8: noqa
    s = [int(i) for i in input().split()]
    _ = input()  # flake8: noqa
    t = [int(j) for j in input().split()]

    print(count(s, t))

if __name__ == '__main__':
    run()