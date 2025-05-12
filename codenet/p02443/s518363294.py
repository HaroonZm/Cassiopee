if __name__ == "__main__":
    num_a = int(input())
    a = list(map(lambda x: int(x), input().split()))
    num_query = int(input())

    for _ in range(num_query):
        begin, end = map(lambda x: int(x), input().split())
        if (0 == begin):
            a[begin: end] = a[end - 1:: -1]
        else:
            a[begin: end] = a[end - 1: begin - 1: -1]

    print(" ".join([str(elem) for elem in a]))