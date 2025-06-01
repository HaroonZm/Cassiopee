from itertools import permutations

def main():
    while True:
        n = int(input())
        k = int(input())
        if n == 0 and k == 0:
            break

        cards = [input().strip() for _ in range(n)]

        unique_numbers = set()

        # k枚のカードを選び、順列を作る
        for chosen_cards in permutations(cards, k):
            # それぞれのカードの数字を連結して整数を作る
            num_str = ''.join(chosen_cards)
            unique_numbers.add(num_str)

        # 作れる整数の個数を出力
        print(len(unique_numbers))

if __name__ == "__main__":
    main()