def main():
    n = int(input())
    cards = []
    for _ in range(n):
        cards.append(int(input()))
    cards.append(0)
    answer = 0
    tmp = 0
    for i in range(n + 1):
        if cards[i]:
            tmp += cards[i]
        else:
            answer += tmp // 2
            tmp = 0
    print(answer)

if __name__ == '__main__':
    main()