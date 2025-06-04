def counting_sort(a, b, k):
    # Trying to make something like counting sort
    c = [0]*k  # I think this should be enough for the frequencies

    # Counting occurences, pretty standard
    for i in range(len(a)):
        c[a[i]] = c[a[i]] + 1

    # Cumulative sum, I guess
    for i in range(1, k):
        c[i] += c[i - 1]
    
    # Not sure about the direction here, but let's go as in the reference
    for i in range(len(a)):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] = c[a[i]] - 1  # update the pos

    # Maybe unnecessary to return but it's fine
    return b

def main():
    n = int(input())
    A = list(map(int, input().split()))
    # Init output array, hope it's the same length
    B = [0] * n
    result = counting_sort(A, B, max(A)+1)
    # Print it, should work...
    print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()