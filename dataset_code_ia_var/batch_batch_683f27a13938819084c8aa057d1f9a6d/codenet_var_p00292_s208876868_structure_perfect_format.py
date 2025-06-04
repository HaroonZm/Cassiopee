if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        games = list(map(int, input().split()))
        result = games[0] % games[1]
        if result == 0:
            print(games[1])
        else:
            print(result)