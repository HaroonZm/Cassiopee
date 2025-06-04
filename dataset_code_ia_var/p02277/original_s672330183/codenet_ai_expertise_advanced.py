from operator import itemgetter
from sys import stdin

def partition(arr, left, right):
    pivot = arr[right][1]
    i = left
    for j in range(left, right):
        if arr[j][1] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_sort(arr, left, right):
    stack = [(left, right)]
    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(arr, p, r)
            # Tail recurse on smaller partition for reduced stack depth
            if (q-p) < (r-q):
                stack.append((q+1, r))
                stack.append((p, q-1))
            else:
                stack.append((p, q-1))
                stack.append((q+1, r))

def grouped_suits(l, num, start):
    return [suit for suit, n in l[start:] if n == num]

def is_stable(orig, sorted_cards):
    idx = 0
    while idx < len(sorted_cards) - 1:
        if sorted_cards[idx][1] == sorted_cards[idx+1][1]:
            num = sorted_cards[idx][1]
            sorted_suits = [suit for suit, n in sorted_cards[idx:] if n == num]
            orig_suits = [suit for suit, n in orig if n == num]
            if sorted_suits != orig_suits[:len(sorted_suits)]:
                return False
            idx += len(sorted_suits)
        else:
            idx += 1
    return True

def main():
    N = int(stdin.readline())
    A = [tuple((suit, int(num))) for suit, num in (stdin.readline().split() for _ in range(N))]
    orig_list = list(A)
    quick_sort(A, 0, N - 1)
    print("Stable" if is_stable(orig_list, A) else "Not stable")
    print('\n'.join(f"{suit} {num}" for suit, num in A))

if __name__ == "__main__":
    main()