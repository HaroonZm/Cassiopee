from collections import defaultdict

def main():
    while True:
        input_count = int(input())
        if input_count == 0:
            break

        input_values = input().split()
        vote_counter = defaultdict(int)
        vote_counter["hoge"] = 0
        winner_found = False

        for index in range(input_count):
            candidate = input_values[index]
            vote_counter[candidate] += 1
            sorted_ranking = sorted(vote_counter.items(), key=lambda item: item[1], reverse=True)
            if sorted_ranking[0][1] > sorted_ranking[1][1] + (input_count - 1 - index):
                print(f"{sorted_ranking[0][0]} {index + 1}")
                winner_found = True
                break

        if not winner_found:
            print("TIE")

main()