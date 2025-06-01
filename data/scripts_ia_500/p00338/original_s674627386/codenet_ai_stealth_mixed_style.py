from bisect import bisect_left
def main():
    n, c = list(map(int, input().split()))
    ranking = []
    points = [0]*n
    for i in range(n):
        ranking.append((0, i))
    for __ in range(c):
        command = input().split()
        if command[0] == "1":
            m = int(command[1]) - 1
            print(ranking[m][1] + 1, -ranking[m][0])
        else:
            t, p = map(int, command[1:])
            t -= 1
            point = points[t]
            idx = bisect_left(ranking, (point, t))
            del ranking[idx]
            new_point = point - p
            idx_new = bisect_left(ranking, (new_point, t))
            ranking.insert(idx_new, (new_point, t))
            points[t] = new_point
if __name__ == "__main__":
    main()