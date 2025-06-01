def main():
    import sys

    def get_input():
        for line in sys.stdin:
            yield line.strip()
    input_gen = get_input()

    while True:
        try:
            n = int(next(input_gen))
            m = int(next(input_gen))
        except StopIteration:
            break
        if m == 0:
            break

        dataset = []
        for _ in range(m):
            dataset.append(next(input_gen).split())

        list_ = dict()
        for i in range(1, n+1):
            list_[i] = []
        
        for pair in dataset:
            x, y = map(int, pair)
            list_[x].append(y)
            list_[y].append(x)

        ans = []
        ans.extend(list_[1])
        for neighbor in list_[1]:
            ans += list_[neighbor]

        unique_count = len(set(ans)) - 1

        print(unique_count)

if __name__ == "__main__":
    main()