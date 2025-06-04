if __name__ == "__main__":
    num_a = int(input())
    a = list(map(int, input().split()))
    num_query = int(input())
    for _ in range(num_query):
        begin, end = map(int, input().split())
        if begin == 0:
            a[begin:end] = a[end-1::-1]
        else:
            a[begin:end] = a[end-1:begin-1:-1]
    print(" ".join(str(elem) for elem in a))