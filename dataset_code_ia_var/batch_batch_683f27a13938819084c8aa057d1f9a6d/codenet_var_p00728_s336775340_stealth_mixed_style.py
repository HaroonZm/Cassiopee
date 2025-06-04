def main():
    from functools import reduce

    scores = []
    collect = lambda n: [int(input()) for _ in range(n)]
    append_score = scores.append

    while True:
        n = int(input())
        if n == 0:
            break

        if n < 3:
            print("n doit être >=3")
            continue

        data = collect(n)
        mn = min(data)
        mx = max(data)
        filtered = list(filter(lambda x: x != mn and x != mx, data))
        if len(filtered) != n - 2:
            # remove only one min and one max
            temp = data.copy()
            temp.remove(mn)
            temp.remove(mx)
            filtered = temp
        res = (reduce(lambda a, b: a + b, filtered)) // (n - 2)
        append_score(res)

    i = 0
    while i < len(scores):
        print(scores[i])
        i += 1

main()